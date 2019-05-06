#!/usr/bin/python3

import time
import re
import string as st
import numpy as np
import argparse
from itertools import zip_longest
from itertools import product

# PARAMS
# ---------------------------------------------------------
DICTIONARY = "./dictionaries/dictionary.txt"


# TOOLS
# ---------------------------------------------------------
def get_ngram(N=1,ngram={
                        'words': {},
                        'monograms': {},
                        'bigrams': {},
                        'trigrams': {},
                        'quadgrams': {}
                        }):
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
             4 - quadgram
Optional parameter ngram is used for memory optimization"""
    ngrams = [
              'words',
              'monograms',
              'bigrams',
              'trigrams',
              'quadgrams'
             ]
    assert N < len(ngrams)
    dictio = ngram[ngrams[N]]
    if not dictio:
        source = './dictionaries/{}'.format(ngrams[N])
        with open(source) as fl:
            data = fl.read().splitlines()
        result = [d.split(' ') for d in data]
        for a,b in result:
            dictio[a.strip()] = float(b)
    return dictio


def clean_datastr(datastr):
    """Removes whitespace and punctuations and returns string uppercased."""
    remove = st.punctuation + st.whitespace
    datastr = re.sub('['+remove+']','',datastr)
    return datastr.upper()


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
        rng = range(0,len(datastr),blocksize)
    for i in rng:
        yield datastr[i:i+blocksize]

def nthletter_group(datastr, blocksize):
    """Yielding every nth-letter-group of each block of given blocksize, e.g.:
"AAABBBCCCDDDD" => 'ABCDD','ABCD','ABCD' (with blocksize=3)
Used for keylength ciphers like Vineger,
too thread every nth letter as their own rot-cipher.
Arguments:
datastr     -- string
blocksize   -- integer (keylength)"""
    letters = [''] * blocksize
    datastr = clean_datastr(datastr)
    for i in range(blocksize):
        nthletters = [datastr[c] for c in range(i,len(datastr),blocksize)]
        yield "".join(nthletters)


def sort_by_value(tuples,reverse=True):
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
        # TODO: fix python lint, correct:
        # data = [head,*data]
        data = [head] + data
        nr_of_rows += 1
    # calculate the column width for each column
    column_width = [max(map(len,map(str,col))) + 2 for col in zip(*data)]
    # Reduce column size for max-width, largest column first
    while sum(column_width) > max_width:
        i = column_width.index(max(column_width))
        column_width[i] -= 1
    def adjust(string,length):
        if len(string) < length:
            return string.ljust(length)
        else:
            # Padding is reduced too 1!
            return string[:length-3] + ".. "
    for row in data[:nr_of_rows]:
        print("".join([adjust(str(attr),column_width[i])
                for i, attr in enumerate(row)]))

# ANALYSE
# ---------------------------------------------------------
def chi_squared(datastr,blocksize=1):
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
    freq = block_freq(datastr,blocksize)
    total = len(datastr)
    chi = 0
    for k,v in freq.items():
        if k in ngram.keys():
            e = total * ngram[k]
        else:
            e = 0.01
        chi += (v-e)**2/e
    return chi


def IC_analyses(datastr, keylength=1):
    """Calculate the IC of each nthletter-grouped block.
For finding the correct Vinegere keylength.

Arguments:
datastr     -- string with data
keylength   -- size of the grouped letters (default 1)"""
    datastr = clean_datastr(datastr)
    if keylength > len(datastr):
        return (0.0,0.0)
    blocks = nthletter_group(datastr, keylength)
    ics = []
    for b in blocks:
        if len(b) >= keylength:
            ics.append(IC(b))
    if len(ics) > 1:
        return (np.mean(ics),np.std(ics))
    elif len(ics) == 1:
        return (ics[0],0.0)
    else:
        return (0.0,0.0)


def relative_block_freq(datastr,blocksize=1):
    """Calculate the block-frequency (shifted) in a datastr
and appends the relative frequency to the data

Arguments:
datastr     -- string with data
blocksize   -- size of the grouped letters (default 1)"""
    freq = block_freq(datastr, blocksize)
    total = len(datastr)
    for b,f in freq.items():
        freq[b] = (f,float(f*len(b))/total)
    return freq


def score_english(text):
    """Try and determin if a text is English. Returns the precentage (float)
of English words found in the text."""
    # Get all the words from the DICTIONARY file
    with open(DICTIONARY) as f:
        english_words = f.read().split()
    # and make sorted list, largest word first
    english_words.sort(key = lambda s: len(s),reverse=True)
    # Calculate a score based on the remaining text
    t = text
    for w in english_words:
        if len(w) > len(t):
            continue
        if w in t:
            t = "".join(t.split(w))
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

If from_alpha doesn't contain enough (26) chars,
the returned alphabeth is filled with remaining letters."""
    EN_ALPHABET = "ETAONISRHLDUCMFWGPYBVKXJQZ"
    key = [''] * 26
    # Make sure alphabets are uppercased
    from_alpha = from_alpha.upper()
    to_alpha = to_alpha.upper()
    for i in range(len(from_alpha)):
        key[ord(from_alpha[i])-65] = to_alpha[i]
    # fill the gaps...
    for i,(k,EN) in enumerate(zip(key,EN_ALPHABET)):
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
    for keylength in range(1,len(datastr)):
        mean, std = IC_analyses(datastr,keylength)
        ics.append((keylength,mean,std))
    return list(filter(lambda ic: ic[1] > 0.06,ics))


def gen_vin_keys(datastr,keylength,interactive=False):
    """With a given keylength, try and find the key for the Vinegere cipher. 
This function uses a rotation on every nthletter-group, and calls find_ROT 
too calculate the chi-squared statistic of the decrypted text.

Arguments:
datastr     -- string
keylength   -- integer
interactive -- boolean (default False)

Returns list of tuples: [(key, mean IC, decypted datastr),...]
If not interactive, the list only contains one tuple.

Asuming the best key is the right key, 
generating more key's is very performance heavy,
hence the optional argument 'interactive'."""
    groups = nthletter_group(datastr,keylength)
    nth_rot = []
    for b in groups:
        nth_rot.append([(rot,ic) for rot,ic,_ in find_ROT(b)[:2]])
    data = []
    # Generate key's
    for p in product(*nth_rot):
        key = ''
        total_ic = 0
        for rot,ic in p:
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
    groups = list(group(datastr,5))
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
    if len(key) != 26:
        print("The length of the key ({}) is too small to use\
               in mono alphabetic cipher, key given: {}".format(len(key),key))
        exit(2)
    if len(set(key)) != 26:
        print("Not a complete alhabet found\
               in mono alphabetic cipher key: {}".format(key))
        exit(2)
    key = key.upper()
    skip = st.punctuation + st.whitespace + st.digits
    result = ''
    for c in datastr:
        if c in skip:
            result += c
        else:
            result += key[ord(c.upper()) - 65].lower()
    return result


# Mono aplhabetic substitution decryption
def alphabetic_decrypt(datastr, key):
    decr_key = alphabetic_compose_key(key, st.ascii_uppercase)
    return alphabetic_encrypt(datastr, decr_key)


# Simple Caesar cipher (ROT#)
def caesar_encrypt(datastr, rott=13):
    result = ''
    for c in datastr:
        result += rot(c, rott)
    return result


def caesar_decrypt(datastr, rott=13):
    return caesar_encrypt(datastr, 26-rott)


# DETECT ENCRYPTION
# ---------------------------------------------------------
def detect_cipher(datastr, key, interactive=False):
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
            for i in range(1,26):
                an.append(IC_analyses(datastr, i)[0])
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
# The program decipher.py reads from sys.args
def main():
    parser = argparse.ArgumentParser(prog='decipher', 
            description='A commandline deCipher tool.',
            epilog="Created by S. Thewessen.")
    parser.add_argument('files', metavar='file',nargs='+',
            help='Input file(s) too encryption/decryption.')
    parser.add_argument('-e','--encode', metavar='encode',
            action='store_const',const=True,default=False,
            help='Run this program too encode the input (default: decode)')
    parser.add_argument('-E','--obfuscate', metavar='obfuscate',
            action='store_const',const=True,default=False,
            help='Even harder encoding by obfuscating the output.\
                  Removes punctuation and whitespace from output,\
                  Makes output uppercase, and groups output by 5 letters.')
    parser.add_argument('-i','--interactive', metavar='interactive',
            action='store_const',const=True,default=False,
            help='Interactive mode.')
    parser.add_argument('-k','--key', metavar='key',
            help='The key too use for the cipher. If the key is an integer,\
                    a basic Caesar Cipher is used.')
    parser.add_argument('-l','--length', metavar='N', type=int,
            help='The length N of the key as an integer (Vinegere)')
    parser.add_argument('-c','--cipher',
            choices=['caesar','alphabetic','vinegere'],
            help='Force a specific cipher too use.')
    parser.add_argument('-f','--frequency-analyses', metavar='N', type=int,
            dest='freq',
            help='Give the frequency analyses of block size N\
                    for the given data.')
    args = parser.parse_args()

    key = None
    data = []
    # Some input handling and error messages
    if args.obfuscate and not args.encrypt:
        args.encrypt = True
    if args.key and args.length:
        if len(args.key) != args.length:
            print("The given key '{}'\
                    and the given length {} are not the same.\
                    Please make sure they are or just ommit the length."\
                    .format(args.key,args.length))
            exit(2)
    if type(args.key) == str:
        for c in st.punctuation:
            if c in args.key:
                if args.encode:
                    e = 'encrypt'
                else:
                    e = 'decrypt'
                print("You can't {} a data string with a key containing '{}'!\
                        Key given: '{}'".format(e, c, args.key))
                exit(2)
    if args.interactive: 
        print("Arguments:")
        for k in vars(args):
            v = getattr(args,k)
            print("{} = {}".format(k,v))
        print('')
    # Setup the right function to use
    def fn(dstr):
        if args.cipher == "caesar":
            if args.key:
                if not args.key.isdigit():
                    print("You need an integer key to use with a rotation cipher!")
                    print("Key given: {}".format(args.key))
                    exit(2)
                else:
                    args.key = int(args.key)
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
                        column_print(result, head=['ROT','chi-squared','text'])
                        print("Rotation {} was used with an chi-squared score of {}."\
                                .format(args.key, round(score,2)))
                        print("Decrypting the message took {} seconds.\n"\
                                .format(round(time.time() - start,3)))
                    return text
                else:
                    return caesar_decrypt(dstr, args.key)
        if args.cipher == "alphabetic":
            if args.key != None:
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
                print(chi_squared(dstr,3))
                # column_print(chi_squared(freq),head=['block','chi'])
        if args.cipher == "vinegere":
            if args.key != None:
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
                    max_number_keys = 1
                    if args.interactive:
                        start = time.time()
                        max_number_keys = 20
                    if not args.length:
                        key_ls = find_vin_keylength(dstr)
                        args.length = np.gcd.reduce([kl[0] for kl in key_ls])
                        if args.interactive:
                            column_print(key_ls, 
                                    head=[
                                            'KL',
                                            'IC-analyses (mean)',
                                            'IC-analyses (standard deviation)'
                                         ])
                            if len(key_ls) > 1:
                                print("The keylength is possibly {}.\n"\
                                        .format(args.length))
                            else:
                                print('')
                    result = gen_vin_keys(dstr,args.length,
                                          interactive=args.interactive)
                    (args.key, score, text) = next(result)
                    if args.interactive:
                        # Generate more key's just to be fancy ; )
                        more_keys = sort_by_value(
                                [next(result) for __ in range(2*args.length)],
                                reverse=False
                            )
                        column_print(
                                [(args.key, score, text)]
                                + more_keys,
                                head=['key','chi-squared (mean)','text'])
                        print("The key {} was used with an average chi-squared score of {}.\n"\
                                .format(args.key, round(score,2)))
                        print("Decrypting the message took {} seconds.\n"\
                                .format(round(time.time() - start,3)))
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
            dstr = clean_datastr(datastr)
            freq = sort_by_value(relative_block_freq(dstr,args.freq))
            # devide over four columns for printing...
            col_L = int(np.ceil(len(freq)/4))
            rows = [c1 + c2 + c3 + c4 for c1,c2,c3,c4 in zip_longest(
                        freq[:col_L],
                        freq[col_L:2*col_L],
                        freq[2*col_L:3*col_L],
                        freq[3*col_L:],
                        fillvalue=('','')
                    )]
            column_print(rows,
                         head=['blk','frequency']*4,
                         max_width=79
                        )
            continue
        if args.interactive: 
            print("Input data:\n {} \n".format(datastr))
        if args.cipher == None:
            if args.interactive: 
                print("No specific cipher was given.")
            args.cipher = detect_cipher(datastr, args.key, args.interactive)
        output = fn(datastr)
        if args.interactive: 
            print("Output data:")
        print(output)

if __name__ == "__main__":
    main()
