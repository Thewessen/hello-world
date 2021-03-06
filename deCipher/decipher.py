#!/usr/bin/python3

import time
import re
import random
import string as st
import numpy as np
import argparse
import sys
# from itertools import zip_longest
from itertools import product

# PARAMS
# ---------------------------------------------------------
# files
DICTIONARY = './dictionaries/dictionary.txt'
WORDS = './dictionaries/words'
MONOGRAMS = './dictionaries/monograms'
BIGRAMS = './dictionaries/bigrams'
TRIGRAMS = './dictionaries/trigrams'
QUADGRAMS = './dictionaries/quadgrams'

# caching
NGRAMS = {0: None,
          1: None,
          2: None,
          3: None,
          4: None}


# TOOLS
# ---------------------------------------------------------
def get_ngram(N=1):
    """Returns corresponding ngram as an dictionary object, e.g.:
bigram = {
    'TH':   0.0270569804001
    'HE':   0.0232854497343
    'IN':   0.0202755339125
    ...
    string: float
}

Arguments:
N       -- ngram integer, choices:
             0 - words
             1 - monogram (default)
             2 - bigram
             3 - trigram
             4 - quadgram"""
    sources = [
                WORDS,
                MONOGRAMS,
                BIGRAMS,
                TRIGRAMS,
                QUADGRAMS
             ]
    assert N < len(sources)
    if NGRAMS[N] is None:
        NGRAMS[N] = {}
        with open(sources[N]) as fl:
            data = fl.read().splitlines()
        result = [d.split(' ') for d in data]
        for a, b in result:
            NGRAMS[N][a.strip()] = float(b)
    return NGRAMS[N]


def clean_datastr(datastr):
    """Removes whitespace and punctuations and returns string uppercased."""
    remove = st.punctuation + st.whitespace
    datastr = re.sub('['+remove+']', '', datastr)
    return datastr.upper()


def remove_extra_spaces(message):
    """Removes extra (more then one) spaces in a string, often caused by
indention. Indention is converted to a space."""
    message = re.sub('^ ', '', message)
    message = re.sub(r'([\n\r]+) ', r'\1', message)
    message = re.sub(r'\t', ' ', message)
    message = re.sub(' +', ' ', message)
    return message


def IC(datastr):
    """Index of Coincidence.
Calculates the IC (Index of Coincidence) of a given string.
Formula: IC = sum( n  * (n - 1) / (N * (N - 1)) )
With...
n: frequency of letter from alphabet in string
N: total number of letters in string
Alphabet: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

Input: string
Return: float

Used for cipher and/or keylength detection"""
    datastr = clean_datastr(datastr)
    n = 0.0
    t = len(datastr)
    t = t * (t - 1)
    for c in st.ascii_uppercase:
        o = datastr.count(c)
        n += o * (o - 1)
    return float(n) / t


def group(datastr, blocksize=1, shift=False):
    """Generate groups of characters in given string, e.g.:
block: 'ABCDE' => 'AB','CD','E' <iterator>
shift: 'ABCDE' => 'AB','BC','CD','DE' <iterator>
Arguments:
datastr     -- string
blocksize   -- integer (default 1)
shift       -- boolean (default False)"""
    datastr = clean_datastr(datastr)
    if shift:
        rng = range(len(datastr)-blocksize+1)
    else:
        rng = range(0, len(datastr), blocksize)
    for i in rng:
        yield datastr[i:i+blocksize]


def nthletter_group(datastr, blocksize):
    """Yielding every nth-letter-group of each block of given blocksize, e.g.:
'AAABBBCCCDDDD' => 'ABCDD','ABCD','ABCD' (with blocksize=3)
Used for keylength ciphers like Vineger,
too thread every nth letter as their own rot-cipher.
Arguments:
datastr     -- string
blocksize   -- integer (keylength)"""
    datastr = clean_datastr(datastr)
    for i in range(blocksize):
        yield ''.join(datastr[i::blocksize])


def sort_by_value(tuples, reverse=True):
    """Sort list of tuples by their second element (used alot)"""
    return sorted(tuples, key=lambda k: k[1], reverse=reverse)


def rot(char, rotate):
    """Rotates an alphabetic char, e.g.:
'A',2 => 'C'
'd',0 => 'd'
'Z',1 => 'A'
...
Arguments:
char    -- single letter string, upper- or lowercase.
rotate  -- integer used for rotation."""
    if char.isupper():
        diff = ord('A')
    elif char.islower():
        diff = ord('a')
    else:
        return char
    nr = ord(char)
    nr -= diff
    nr += rotate
    nr %= 26
    nr += diff
    return chr(nr)


def block_freq(datastr, blocksize=1, shift=True):
    """Returns a sorted list of frequencies of each block/group of characters
contained in the datastring, e.g.: [('TH',1337),(str,int),...]

Arguments:
datastr     -- string
blocksize   -- integer of group size (default 1)
shift       -- boolean if a group(,,shift) is to be used (default True)"""
    datastr = clean_datastr(datastr)
    blocks = group(datastr, blocksize, shift)
    diction = {}
    for b in blocks:
        if b not in diction:
            diction[b] = 1
        else:
            diction[b] += 1
    return diction


def column_print(data, head=[], nr_of_rows=0, max_width=79):
    """Prints the given data in nice columns.

Arguments:
data        --  list of rows (list of list)
head        --  optional list of heading for columns (default [])
nr_of_rows  --  optional integer of rows to be printed,
                not including the head (default everything)
max_width   --  integer for the maximum total width (default 79)"""
    if not nr_of_rows:
        nr_of_rows = len(data)
    if head:
        data = [head] + data
        nr_of_rows += 1
    # calculate the column width for each column
    column_width = [max(map(len, map(str, col))) + 2 for col in zip(*data)]
    # Reduce column size for max-width, largest column first
    while sum(column_width) > max_width:
        i = column_width.index(max(column_width))
        column_width[i] -= 1

    def adjust(string, length):
        if len(string) < length:
            return string.ljust(length)
        else:
            # Padding is reduced too 1!
            return string[:length-3] + '.. '

    for row in data[:nr_of_rows]:
        print(''.join([adjust(str(attr), column_width[i])
                      for i, attr in enumerate(row)]))


# ANALYSE
# ---------------------------------------------------------
def chi_squared(datastr, blocksize=1):
    """Calculate the chi-squared statistic of a given data string.
This statistic is used to compare two distributions.
Formula: chi-squared = sum( (Fd - Fe)**2 / Fe )
With...
Fd: Frequency of block/char in the datastring
Fe: Expected frequency of block/char in the datastring

Arguments:
datastr     -- string with data
blocksize   -- size of the grouped letters (default 1)
ngram       -- ngram to use for reference

The expected frequency is calculated by: len(datastring)*ngram-statistic(char),
where ngram-statistic is the relative frequency in the english dictionary."""
    ngram = get_ngram(blocksize)
    freq = block_freq(datastr, blocksize)
    total = len(datastr)
    chi = 0
    for k, v in freq.items():
        if k in ngram.keys():
            e = total * ngram[k]
        else:
            e = 0.01
        chi += (v-e)**2/e
    return chi


def keylength_analyses(datastr, keylength=1):
    """Calculate the IC of each nthletter-grouped block.
For finding the correct Vinegere keylength.

Arguments:
datastr     -- string with data
keylength   -- size of the grouped letters (default 1)"""
    datastr = clean_datastr(datastr)
    if keylength > len(datastr):
        return (0.0, 0.0)
    blocks = nthletter_group(datastr, keylength)
    ics = []
    for b in blocks:
        if len(b) >= keylength:
            ics.append(IC(b))
    if len(ics) > 1:
        return (np.mean(ics), np.std(ics))
    elif len(ics) == 1:
        return (ics[0], 0.0)
    else:
        return (0.0, 0.0)


def relative_block_freq(datastr, blocksize=1):
    """Calculate the block-frequency (shifted) in a datastr
and appends the relative frequency to the data

Arguments:
datastr     -- string with data
blocksize   -- size of the grouped letters (default 1)"""
    freq = block_freq(datastr, blocksize)
    total = len(datastr)
    for b, f in freq.items():
        freq[b] = (f, float(f*len(b))/total)
    return freq


def score_english(text):
    """Try and determin if a text is English. Returns the precentage (float)
of English words found in the text."""
    # Get all the words from the DICTIONARY file
    with open(DICTIONARY) as f:
        english_words = f.read().split()
    # and make sorted list, largest word first
    english_words.sort(key=lambda s: len(s), reverse=True)
    # Calculate a score based on the remaining text
    t = text
    for w in english_words:
        if len(w) > len(t):
            continue
        if w in t:
            t = ''.join(t.split(w))
        if len(t) == 0:
            break
    return float(len(text) - len(t)) / len(text) * 100


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
            chi_squared(text),
            text
           )
        )
    return sort_by_value(result, reverse=False)


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
    EN_ALPHABET = 'ETAONISRHLDUCMFWGPYBVKXJQZ'
    key = [''] * 26
    # Clean key's
    from_alpha = clean_datastr(from_alpha)
    to_alpha = clean_datastr(to_alpha)
    for i in range(len(from_alpha)):
        key[ord(from_alpha[i])-65] = to_alpha[i]
    # fill the gaps...
    for i, (k, EN) in enumerate(zip(key, EN_ALPHABET)):
        if k == '':
            key[i] = EN
    return ''.join(key)


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
    groups = nthletter_group(datastr, keylength)
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
    datastr = clean_datastr(datastr)
    groups = list(group(datastr, 5))
    return ' '.join(groups)


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
    key = clean_datastr(key)
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
Input: 'Hello my dear friends!'
Key: 'QLNEHPAYUZRGIBXKWDOJSCVFMT' (means: A -> Q, B -> L, etc.)
Output: 'Yhggx im ehqd pduhbeo!'
NOTE: All punctuation and whitespace is removed from the key.
The key has to contain all letters of the (English) alphabet.
Punctuations, whitespace and digits in the datastring are skipped.

Arguments:
datastr     -- string containing the text to encrypt
key         -- string of letters containing the alphabet bijection"""
    key = clean_datastr(key)
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


def alphabetic_decrypt(datastr, key):
    """Decrypting a mono-alphabetic substitution cipher.
The given key is inversed.

Arguments:
datastr     -- string containing the text to decrypt
key         -- string containing the alphabet bijection for encryption"""
    decr_key = alphabetic_compose_key(key, st.ascii_uppercase)
    return alphabetic_encrypt(datastr, decr_key)


def caesar_encrypt(datastr, key=13):
    """A Caesar cipher uses rotation of the characters as they appear
in the (English) alphabet, e.g.:
Input: 'Hello world!'
key: 9
Output: 'Qnuux fxaum!'
If key 13 is used, the cipher is also called ROT13

Arguments:
datastr     -- string containing the text to encrypt
rott        -- the rotating key too use (default 13)"""
    result = ''
    for c in datastr:
        result += rot(c, key)
    return result


def caesar_decrypt(datastr, key=13):
    """Decrypting a Caesar cipher, by rotating the datastring back.
See caesar_encrypt.__doc__ for more information.

Arguments:
datastr     -- string containing the text to encrypt
rott        -- the rotating key too use (default 13)"""
    return caesar_encrypt(datastr, 26-key)


# DETECT ENCRYPTION
# ---------------------------------------------------------
def detect_cipher(datastr, key, interactive=False):
    """Trying to detect which decryption to use for a given text."""
    # TODO Finish this function and __doc__
    cipher = ''
    if key:
        if key.isdigit():
            key = int(key)
            cipher = 'caesar'
        else:
            cipher = 'vinegere'
    else:
        if len(datastr) >= 26:
            an = []
            for i in range(1, 26):
                an.append(keylength_analyses(datastr, i)[0])
            dev = np.std(an)
            if dev < 0.003:
                cipher = 'caesar'
            else:
                cipher = 'vinegere'
        else:
            cipher = 'caesar'
            if interactive:
                message = 'Data string is too small\
                           to determin which cipher to use.'
                print(remove_extra_spaces(message))
    if interactive:
        message = 'Trying to use a {} cipher\
                   for the data string.\n'.format(cipher)
        print(remove_extra_spaces(message))
    return cipher


def decrypt_caesar_without_key(datastr, interactive=False, **kwargs):
    if interactive:
        start = time.time()
    result = find_ROT(datastr)
    (key, score, text) = result[0]
    if interactive:
        column_print(result,
                     head=['ROT', 'chi-squared', 'text'])
        message = 'Rotation {} was used with an chi-squared\
                   score of {}.\n'.format(key, round(score, 2))
        # '+=' only way to not indent Decrypting with a space
        message += 'Decrypting the message took {} seconds.\n'\
                   .format(round(time.time() - start, 3))
        message = remove_extra_spaces(message)
        print(message)
    return text


def decrypt_vinegere_without_key(datastr, length=None, interactive=False):
    if interactive:
        start = time.time()
    if length is None:
        key_ls = find_vin_keylength(datastr)
        length = np.gcd.reduce([kl[0] for kl in key_ls])
        if interactive:
            column_print(key_ls,
                         head=[
                            'KL',
                            'IC-analyses (mean)',
                            'IC-analyses (standard deviation)'
                         ])
            if len(key_ls) > 1:
                message = 'The keylength is possibly {}.\n'\
                          .format(length)
                print(message)
            else:
                print('')
    result = gen_vin_keys(datastr, length)
    (key, score, text) = next(result)
    if interactive:
        # Generate more key's just to be fancy ; )
        more_keys = sort_by_value(
                [next(result) for __ in range(2*length)],
                reverse=False
            )
        column_print(
                [(key, score, text)] + more_keys,
                head=['key', 'chi-squared (mean)', 'text'])
        message = 'The key {} was used with an average\
                   chi-squared score of {}.\n\
                   Decrypting the message took {} seconds.'\
                  .format(key,
                          round(score, 2),
                          round(time.time() - start, 3))
        message = remove_extra_spaces(message)
        print(message)
        print('')
    return text


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
    if args.key is not None\
        and args.length is not None\
            and len(args.key) != args.length:
        message = "Error: the given key '{}' and the given length {}\
                   are not the same!\n Ommiting the keylength..."\
                   .format(args.key, args.length)
        message = remove_extra_spaces(message)
        print(message, file=sys.stderr)
        args.length = None
    # No punctuations and/or whitespace in a given key
    if args.key is not None:
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
    if args.key is not None and args.key.isdigit():
        args.key = int(args.key)
        args.cipher = 'caesar'
    elif args.key is not None and args.cipher == 'caesar':
        message = 'You need an integer key to use with a caesar cipher!\n'
        message += 'Key given: ' + args.key
        parser.error(message)
    # An alphabetic key has to contain all letters of the alphabet
    if args.cipher == 'alphabetic' and args.key is not None:
        key = args.key
        if len(key) != 26:
            message = 'The length of the key ({}) is too small to use\
                       in mono alphabetic cipher, key given: {}'\
                       .format(len(key), key)
            parser.error(message)
        elif len(set(key)) != 26:
            message = 'Not a complete alhabet found\
                       in mono alphabetic cipher key: {}'\
                       .format(key)
            parser.error(message)
    # A key for the Vineger cipher can't contain digits...
    # Already checked for punctuations in any given key
    if args.cipher == 'vinegere' and args.key is not None:
        digits = re.compile('['+st.digits+']')
        if digits.search(args.key):
            message = "You can't use digits in a Vigenere cipher key!\n"
            message += 'Key given: ' + args.key
            parser.error(message)
    # Generate a random key when no key is given...
    if args.cipher == 'caesar' and args.encode and args.key is None:
        message = 'No rotation given for encoding the data using a\
                   Caesar rotation cipher!\n'
        sec_random = random.SystemRandom()
        args.key = sec_random.randint(1, 26)
        message += 'Using rotation: {}'.format(args.key)
        message = remove_extra_spaces(message)
        print(message, file=sys.stderr)
    if args.cipher == 'alphabetic' and args.encode and args.key is None:
        message = 'No key given for encoding the data using mono\
                   alphabetic substitution cipher!\
                   Generating a random key...\n'
        alpha = list(st.ascii_uppercase)
        random.shuffle(alpha)
        args.key = ''.join(alpha)
        message += 'Using key: {}'.format(args.key)
        message = remove_extra_spaces(message)
        print(message, file=sys.stderr)
    if args.cipher == 'vinegere' and args.encode and args.key is None:
        message = 'No key given for encoding the data using Vineger\
                   encryption! Generating a random key using a word list\
                   ...\n'
        with open(DICTIONARY) as di:
            words = di.read().splitlines()
        sec_random = random.SystemRandom()
        args.key = ''
        while len(args.key) < 9:
            args.key += sec_random.choice(words)
        message += 'Using key: {}'.format(args.key)
        message = remove_extra_spaces(message)
        print(message, file=sys.stderr)
    # Frequency analyses only possible for blocksize 1-4...
    if args.freq is not None and args.freq not in range(1, 5):
        message = 'Frequency analyses with a blocksize of {} is\
                   currently not possible.'.format(args.freq)
        message = remove_extra_spaces(message)
        parser.error(message)


def main():
    """Main function of the program. Uses argparse too read from stdin.
See decipher.py -h for a brief help of it's functionality"""
    parser = argparse.ArgumentParser(prog='decipher',
                                     description='A commandline\
                                             deCipher tool.',
                                     epilog='Created by S. Thewessen.')
    parser.add_argument('files',  metavar='file', nargs='+',
                        help='Input file(s) too encryption/decryption.')
    parser.add_argument('-i', '--interactive', action='store_const',
                        const=True, default=False,
                        help='Interactive mode.')
    parser.add_argument('-c', '--cipher',
                        choices=['caesar', 'alphabetic', 'vinegere'],
                        help='Force a specific cipher too use.')
    parser.add_argument('-k', '--key',
                        help='The key too use for the cipher.\
                              If the key is an integer, \
                              a basic Caesar Cipher is used.')
    parser.add_argument('-l', '--length',  metavar='N',  type=int,
                        help='The length N of the key as an integer.')
    parser.add_argument('-e', '--encode',  action='store_const',
                        const=True, default=False,
                        help='Run this program too encode the input\
                              (default: decode)')
    parser.add_argument('-E', '--encode-obfuscate',
                        dest='obfuscate', action='store_const',
                        const=True, default=False,
                        help='Even harder encoding by obfuscating the output.\
                              Removes punctuation and whitespace from output,\
                              Makes output uppercase,\
                              and groups output by 5 letters.')
    parser.add_argument('-f', '--frequency-analyses',  metavar='N',  type=int,
                        dest='freq',
                        help='Give the frequency analyses of block size N\
                              for the given data, printed side by side.\
                              No encryption or decryption is used when\
                              this option is set. Only blocksizes between 1\
                              and 4 are valid!')
    args = parser.parse_args()
    if args.interactive:
        print('Arguments:')
        for k in vars(args):
            v = getattr(args, k)
            print('{} = {}'.format(k, v))
        print('')
    args_settings(args, parser)

    # Setup the right function to use
    def fn(dstr):
        if args.encode:
            cipher = {
                'caesar': caesar_encrypt,
                'alphabetic': alphabetic_encrypt,
                'vinegere': vinegere_encrypt
            }[args.cipher]
            result = cipher(dstr, key=args.key)
            if args.obfuscate is None:
                return result
            else:
                return obfuscate(result)
        else:
            if args.key is not None:
                cipher = {
                    'caesar': caesar_decrypt,
                    'alphabetic': alphabetic_decrypt,
                    'vinegere': vinegere_decrypt
                }[args.cipher]
                return cipher(dstr, key=args.key)
            else:
                cipher = {
                    'caesar': decrypt_caesar_without_key,
                    'alphabetic': None,
                    'vinegere': decrypt_vinegere_without_key
                }[args.cipher]
                return cipher(dstr, length=args.length,
                              interactive=args.interactive)
    datastr = ''
    clm_rows = []
    for d in args.files:
        with open(d) as fl:
            datastr = fl.read().strip()
        if args.freq is not None:
            dstr = clean_datastr(datastr)
            freq = relative_block_freq(dstr, args.freq)
            freq = [(k, f, round(r, 3)) for k, (f, r) in freq.items()]
            freq = sort_by_value(freq)
            # Collect data for column_print
            clm_rows.append(freq)
            continue
        if args.interactive:
            print('Input data:\n {} \n'.format(datastr))
        if not args.cipher:
            if args.interactive:
                print('No specific cipher was given.')
            args.cipher = detect_cipher(datastr, args.key, args.interactive)
        output = fn(datastr)
        if args.interactive:
            print('Output data:')
        print(output)
    if args.freq is not None:
        rows = []
        # The corresponding regular English ngram in the first column
        first_col = [(b, round(r, 6))
                     for b, r in get_ngram(args.freq).items()]
        # The first column has to be the longest column, otherwise the fill
        # won't add up...
        # for z in zip_longest(first_col, *clm_rows, fillvalue=('', '', '')):
        #
        # Or without longest column printing...
        for z in zip(first_col, *clm_rows):
            row = ()
            for multi in z:
                row += multi
            rows.append(row)
        try:
            column_print(rows,
                         head=['blk', 'relative']
                         + ['blk', 'freq', 'relative']*len(clm_rows),
                         max_width=120)
        except BrokenPipeError:
            sys.exit(0)


if __name__ == '__main__':
    main()
