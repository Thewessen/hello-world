#!/usr/bin/python3

import utils
import re
import string as st
import numpy as np
import time
import argparse
import sys
from itertools import zip_longest
from itertools import product


# CAESAR ROT
# ---------------------------------------------------------
def rot(char, rotate):
    """Rotates an alphabetic char, e.g.:
'A',2 => 'C'
'd',0 => 'd'
'Z',1 => 'A'
...
Arguments:
char    -- single letter string, upper- or lowercase.
rotate  -- integer used for rotation."""
    nr = ord(char)
    if char.isupper():
        diff = ord('A')
    elif char.islower():
        diff = ord('a')
    else:
        return char
    nr -= diff
    nr += rotate
    nr %= 26
    nr += diff
    return chr(nr)


def keylength_analyses(datastr, keylength=1):
    """Calculate the IC of each nthletter-grouped block.
For finding the correct Vinegere keylength.

Arguments:
datastr     -- string with data
keylength   -- size of the grouped letters (default 1)"""
    datastr = utils.clean_datastr(datastr)
    if keylength > len(datastr):
        return (0.0, 0.0)
    blocks = utils.nthletter_group(datastr, keylength)
    ics = []
    for b in blocks:
        if len(b) >= keylength:
            ics.append(utils.IC(b))
    if len(ics) > 1:
        return (np.mean(ics), np.std(ics))
    elif len(ics) == 1:
        return (ics[0], 0.0)
    else:
        return (0.0, 0.0)


# FIND KEYS
# ---------------------------------------------------------
def find_ROT(datastr):
    """Given a datastr, try every 26 (alphabet) rotations of
characters and calculate the chi-squared of each result.
Returning, sorted by lowest chi-squared first:
[(rotation, chi-squared, rotated-text),
 (int     , float      , string      ), ... ]"""
    result = []
    for i in range(26):
        text = caesar_decrypt(datastr, i)
        result.append(
           (
            i,
            utils.chi_squared(text),
            text
           )
        )
    return utils.sort_by_value(result, reverse=False)


def alphabetic_compose_key(from_alpha, to_alpha):
    """Composes a new bijection (mapping) from
'ABCDEFGHIJKLMNOPQRSTUVWXYZ' too a new alphabet, where
'from_alpha' is the old bijection, e.g.:
from:   'ETAONISRHLDUCMFWGPYBVKXJQZ'
to:     'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
return: 'CTMKAOQIFXVJNEDRYHGBLUPWSZ' (inverse substitution)

from:   'ETAONISRHLDUCMFWGPYBVKXJQZ'
to:     'ETAONISRHLDUCMFWGPYBVKXJQZ'
return: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

Arguments:
from_aplha  -- Old bijection.
to_alpha    -- New bijection.

NOTE: If from_alpha doesn't contain enough (26) chars,
the returned alphabeth is filled with remaining letters.
Any whitespace or punctuations is removed from the key"""
    # English alphabet in order of occurence in natural language
    EN_ALPHABET = "ETAONISRHLDUCMFWGPYBVKXJQZ"
    key = [''] * 26
    # Clean key's
    from_alpha = utils.clean_datastr(from_alpha)
    to_alpha = utils.clean_datastr(to_alpha)
    for i in range(len(from_alpha)):
        key[ord(from_alpha[i])-65] = to_alpha[i]
    # fill the gaps...
    for i, (k, EN) in enumerate(zip(key, EN_ALPHABET)):
        if k == '':
            key[i] = EN
    return "".join(key)


def find_vin_keylength(datastr):
    """Find the keylength of a Vinegere encryption,
by calculating the IC of keylength 1 to the length of the datastr.
Returns a filtered list of tuples:
[(keylength,mean IC,standerd deviation IC), ...]
with IC's greater then 0.06."""
    ics = []
    for keylength in range(1, len(datastr)):
        mean, std = keylength_analyses(datastr, keylength)
        ics.append((keylength, mean, std))
    return list(filter(lambda ic: ic[1] > 0.06, ics))


def gen_vin_keys(datastr, keylength):
    """With a given keylength, try and find the key for the Vinegere cipher.
This function uses a rotation on every nthletter-group, and calls find_ROT
too calculate the chi-squared statistic of the decrypted text.

Arguments:
datastr     -- string
keylength   -- integer

Returns list of tuples: [(key, mean IC, decypted datastr),...]
If not interactive, the list only contains one tuple.

Asuming the best key is the right key,
generating more key's is very performance heavy,
hence the optional argument 'interactive'."""
    groups = utils.nthletter_group(datastr, keylength)
    nth_rot = []
    for b in groups:
        nth_rot.append([(rot, ic) for rot, ic, __ in find_ROT(b)[:2]])
    # Generate key's
    for p in product(*nth_rot):
        key = ''
        total_ic = 0
        for rot, ic in p:
            key += chr(rot+65)
            total_ic += ic
        yield (
                 key,
                 float(total_ic)/keylength,
                 vinegere_decrypt(datastr, key)
              )


# ENCRYPT/DECRYPT
# ---------------------------------------------------------
def obfuscate(datastr):
    """Removes punctuations and whitespace,
makes uppercase, and groups by 5 chars/letters"""
    datastr = utils.clean_datastr(datastr)
    groups = list(utils.group(datastr, 5))
    return " ".join(groups)


def vinegere(datastr, key, fn):
    """The Vinegere cipher uses a fixed key, and works
like a ROT cipher, e.g.:
datastr = H  E  L  L  O
integer = 8  5  12 12 15
key     = P  A  S  S  W  O  R  D
integer = 16 1  19 19 23 ...
add     = 24 6  5  5  2
encypt  = X  F  E  E  B

Arguments:
datastr     -- string containing text
key         -- key containing ascii uppercase letters
fn          -- function for calculating ROT (encrypt/decrypt)
Only letters whill be encrypted, everything else is skipped!"""
    result = ''
    key = utils.clean_datastr(key)
    i = 0
    for c in datastr:
        if c in st.ascii_letters:
            k = key[i % len(key)]
            result += rot(datastr[i], fn(ord(k)))
            i += 1
    return result


def vinegere_encrypt(datastr, key):
    """Vineger encryptions, see vineger()..."""
    return vinegere(datastr, key, lambda k: (k - 65))


def vinegere_decrypt(datastr, key):
    """Vineger decryption, see vineger()..."""
    return vinegere(datastr, key, lambda k: 26 - (k - 65))


# Mono aplhabetic substitution encryption
def alphabetic_encrypt(datastr, key):
    """Mono alphabetic substitution cipher uses a bijection
between one alphabet and another to encrypt a message, e.g.:
Input: "Hello my dear friends!"
Key: 'QLNEHPAYUZRGIBXKWDOJSCVFMT' (means: A -> Q, B -> L, etc.)
Output: 'Yhggx im ehqd pduhbeo!'
NOTE: All punctuation and whitespace is removed from the key.
The key has to contain all letters of the (English) alphabet.
Punctuations, whitespace and digits in the datastring are skipped.

Arguments:
datastr     -- string containing the text to encrypt
key         -- string of letters containing the alphabet bijection"""
    key = utils.clean_datastr(key)
    result = ''
    for c in datastr:
        if c in st.ascii_letters:
            r = key[ord(c.upper()) - 65]
            if c.isupper():
                result += r
            else:
                result += r.lower()
        else:
            result += c
    return result


# Mono aplhabetic substitution decryption
def alphabetic_decrypt(datastr, key):
    """Decrypting a mono-alphabetic substitution cipher.
The given key is inversed.

Arguments:
datastr     -- string containing the text to decrypt
key         -- string containing the alphabet bijection for encryption"""
    decr_key = alphabetic_compose_key(key, st.ascii_uppercase)
    return alphabetic_encrypt(datastr, decr_key)


# Simple Caesar cipher (ROT#)
def caesar_encrypt(datastr, rott=13):
    """A Caesar cipher uses rotation of the characters as they appear
in the (English) alphabet, e.g.:
Input: "Hello world!"
key: 9
Output: Qnuux fxaum!
If key 13 is used, the cipher is also called ROT13

Arguments:
datastr     -- string containing the text to encrypt
rott        -- the rotating key too use (default 13)"""
    result = ''
    for c in datastr:
        result += rot(c, rott)
    return result


def caesar_decrypt(datastr, rott=13):
    """Decrypting a Caesar cipher, by rotating the datastring back.
See caesar_encrypt.__doc__ for more information.

Arguments:
datastr     -- string containing the text to encrypt
rott        -- the rotating key too use (default 13)"""
    return caesar_encrypt(datastr, 26-rott)


# DETECT ENCRYPTION
# ---------------------------------------------------------
def detect_cipher(datastr, key, interactive=False):
    """Trying to detect which decryption to use for a given text."""
    # TODO Finish this function and __doc__
    cipher = ''
    if key:
        if key.isdigit():
            key = int(key)
            cipher = "caesar"
        else:
            cipher = "vinegere"
    else:
        if len(datastr) >= 26:
            an = []
            for i in range(1, 26):
                an.append(keylength_analyses(datastr, i)[0])
            dev = np.std(an)
            if dev < 0.003:
                cipher = "alphabetic"
            else:
                cipher = "vinegere"
        else:
            if interactive:
                print("Data string is too small\
                        to determin which cipher to use.")
            cipher = "caesar"
    if interactive:
        print("Trying to use a(n) {} cipher\
                for the data string.".format(cipher))
    return cipher


# MAIN PROGRAM
# ---------------------------------------------------------
def args_settings(args, parser):
    """Helper function for input handling and error messages.
Arguments:
args    -- parser.parse_args() object
parser  -- argparse.ArgumentParser"""
    # obfuscate implies encyption
    if args.obfuscate:
        args.encrypt = True
    # keylength and length key should correspond
    if args.key and args.length and len(args.key) != args.length:
        message = "Error: the given key '{}' and the given length {}\
                   are not the same!\n Ommiting the keylength..."\
                   .format(args.key, args.length)
        message = utils.remove_extra_spaces(message)
        print(message, file=sys.stderr)
        args.length = None
    # No punctuations and/or whitespace in a given key
    if args.key:
        punctuations = re.compile('['+st.punctuation+st.whitespace+']')
        match = punctuations.findall(args.key)
        if match:
            match = set(sorted(match))
            subst = '{} or ' * (len(match) - 1) + '{}'
            subst = "You can't use " + subst + ' in a cipher key!\n'
            message = subst.format(*match)
            message += 'Key given: ' + args.key
            parser.error(message)
    # An integer key means a rot cipher visa versa
    if args.key and args.key.isdigit():
        args.key = int(args.key)
        args.cipher = 'caesar'
    elif args.key and args.cipher == 'caesar':
        message = "You need an integer key to use with a caesar cipher!\n"
        message += "Key given: " + args.key
        parser.error(message)
    # An alphabetic key has to contain all letters of the alphabet
    if args.cipher == 'alphabetic' and args.key:
        key = args.key
        if len(key) != 26:
            message = "The length of the key ({}) is too small to use\
                       in mono alphabetic cipher, key given: {}"\
                       .format(len(key), key)
            parser.error(message)
        elif len(set(key)) != 26:
            message = "Not a complete alhabet found\
                       in mono alphabetic cipher key: {}"\
                       .format(key)
            parser.error(message)
    # A key for the Vineger cipher can't contain digits...
    # Already checked for punctuations in any given key
    if args.cipher == 'vinegere' and args.key:
        digits = re.compile('[' + st.digits + ']')
        match = digits.findall(args.key)
        if digits.search(args.key):
            message = "You can't use digits in a Vigenere cipher key!\n"
            message += 'Key given: ' + args.key
            parser.error(message)


def main():
    """Main function of the program. Uses argparse too read from stdin.
See decipher.py -h for a brief help of it's functionality"""
    parser = argparse.ArgumentParser(prog='decipher',
                                     description='A commandline\
                                             deCipher tool.',
                                     epilog="Created by S. Thewessen.")
    parser.add_argument('files',  metavar='file', nargs='+',
                        help='Input file(s) too encryption/decryption.')
    parser.add_argument('-e', '--encode',  metavar='encode',
                        action='store_const', const=True, default=False,
                        help='Run this program too encode the input\
                              (default: decode)')
    parser.add_argument('-E', '--encode-obfuscate',  metavar='obfuscate',
                        dest='obfuscate', action='store_const',
                        const=True, default=False,
                        help='Even harder encoding by obfuscating the output.\
                              Removes punctuation and whitespace from output,\
                              Makes output uppercase,\
                              and groups output by 5 letters.')
    parser.add_argument('-i', '--interactive', metavar='interactive',
                        action='store_const', const=True, default=False,
                        help='Interactive mode.')
    parser.add_argument('-k', '--key',  metavar='key',
                        help='The key too use for the cipher.\
                              If the key is an integer, \
                              a basic Caesar Cipher is used.')
    parser.add_argument('-l', '--length',  metavar='N',  type=int,
                        help='The length N of the key as an integer.')
    parser.add_argument('-c', '--cipher',
                        choices=['caesar', 'alphabetic', 'vinegere'],
                        help='Force a specific cipher too use.')
    parser.add_argument('-f', '--frequency-analyses',  metavar='N',  type=int,
                        dest='freq',
                        help='Give the frequency analyses of block size N\
                              for the given data.')
    args = parser.parse_args()
    args_settings(args, parser)
    if args.interactive:
        print("Arguments:")
        for k in vars(args):
            v = getattr(args, k)
            print("{} = {}".format(k, v))
        print('')
    # Setup the right function to use

    def fn(dstr):
        if args.cipher == "caesar":
            if args.encode:
                if not args.key:
                    args.key = 13
                result = caesar_encrypt(dstr, args.key)
                if args.obfuscate:
                    return obfuscate(result)
                else:
                    return result
            else:
                if not args.key:
                    if args.interactive:
                        start = time.time()
                    result = find_ROT(dstr)
                    (args.key, score, text) = result[0]
                    if args.interactive:
                        utils.column_print(
                                result,
                                head=['ROT', 'chi-squared', 'text'])
                        message = "Rotation {} was used with an chi-squared\
                                   score of {}.\n\
                                   Decrypting the message took {} seconds.\n"\
                                   .format(args.key,
                                           round(score, 2),
                                           round(time.time() - start, 3))
                        message = utils.remove_extra_spaces(message)
                        print(message)
                    return text
                else:
                    return caesar_decrypt(dstr, args.key)
        if args.cipher == "alphabetic":
            if args.key:
                if args.encode:
                    result = alphabetic_encrypt(dstr, args.key)
                    if args.obfuscate:
                        return obfuscate(result)
                    else:
                        return result
                else:
                    return alphabetic_decrypt(dstr, args.key)
            else:
                # TODO: Find the key!!
                # freq = block_freq(dstr,3)
                print(utils.chi_squared(dstr, 3))
                # utils.column_print(utils.chi_squared(freq),head=['block','chi'])
        if args.cipher == "vinegere":
            if args.key:
                if args.encode:
                    result = vinegere_encrypt(dstr, args.key)
                    if args.obfuscate:
                        return obfuscate(result)
                    else:
                        return result
                else:
                    return vinegere_decrypt(dstr, args.key)
            else:
                if args.encode:
                    print("Give an alphabetic key too use for encoding:")
                    args.key = input()
                    result = vinegere_encrypt(dstr, args.key)
                    if args.obfuscate:
                        return obfuscate(result)
                    else:
                        return result
                else:
                    if args.interactive:
                        start = time.time()
                    if not args.length:
                        key_ls = find_vin_keylength(dstr)
                        args.length = np.gcd.reduce([kl[0] for kl in key_ls])
                        if args.interactive:
                            utils.column_print(
                                key_ls,
                                head=['KL', 'IC-analyses (mean)',
                                      'IC-analyses (standard deviation)']
                            )
                            if len(key_ls) > 1:
                                message = "The keylength is possibly {}.\n"\
                                          .format(args.length)
                                print(message)
                            else:
                                print('')
                    result = gen_vin_keys(dstr, args.length)
                    (args.key, score, text) = next(result)
                    if args.interactive:
                        # Generate more key's just to be fancy ; )
                        more_keys = utils.sort_by_value(
                                [next(result) for __ in range(2*args.length)],
                                reverse=False
                            )
                        utils.column_print(
                                [(args.key, score, text)] + more_keys,
                                head=['key', 'chi-squared (mean)', 'text'])
                        message = "The key {} was used with an average\
                                   chi-squared score of {}.\n\
                                   Decrypting the message took {} seconds.\n"\
                                  .format(args.key,
                                          round(score, 2),
                                          round(time.time() - start, 3))
                        message = utils.remove_extra_spaces(message)
                        print(message)
                        print('')
                    return text
    datastr = ''
    for d in args.files:
        try:
            f = open(d)
            datastr = f.read()
            f.close()
        except Exception as e:
            print(e)
            exit(2)
        datastr = datastr.strip()
        if args.freq:
            dstr = utils.clean_datastr(datastr)
            freq = utils.sort_by_value(
                    utils.relative_block_freq(dstr, args.freq)
                   )
            # devide over four columns for printing...
            col_L = int(np.ceil(len(freq)/4))
            rows = [c1 + c2 + c3 + c4 for c1, c2, c3, c4 in zip_longest(
                        freq[:col_L],
                        freq[col_L:2*col_L],
                        freq[2*col_L:3*col_L],
                        freq[3*col_L:],
                        fillvalue=('', '')
                    )]
            utils.column_print(
                rows,
                head=['blk', 'frequency']*4,
                max_width=79
            )
        if args.interactive:
            print("Input data:\n {} \n".format(datastr))
        if not args.cipher:
            if args.interactive:
                print("No specific cipher was given.")
            args.cipher = detect_cipher(datastr, args.key, args.interactive)
        output = fn(datastr)
        if args.interactive:
            print("Output data:")
        print(output)


if __name__ == "__main__":
    main()
