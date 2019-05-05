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
def get_ngram(N=1):
    """Opens the corresponding ngram data from a file.
And returns it as an dictionary object, e.g.:
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
    ngrams = [
              'words',
              'monograms',
              'bigrams',
              'trigrams',
              'quadgrams'
             ]
    assert N < len(ngrams)
    source = './dictionaries/{}'.format(ngrams[N])
    with open(source) as fl:
        data = fl.read().splitlines()
    result = [d.split(' ') for d in data]
    dictio = {}
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
    """Create groups of characters in given string, e.g.:
block: 'ABCDE' => ['AB','CD','E']
shift: 'ABCDE' => ['AB','BC','CD','DE']
Arguments:
datastr     -- string
blocksize   -- integer (default 1)
shift       -- boolean (default False)"""
    datastr = clean_datastr(datastr)
    if shift:
        return [datastr[i:i+blocksize] for i in range(len(datastr)-blocksize+1)]
    else:
        return [datastr[i:i+blocksize] for i in range(0,len(datastr),blocksize)]

def nthletter_group(datastr, blocksize):
    """Group every nth letter of each block of given blocksize, e.g.:
"AAABBBCCCDDDD" => ['ABCDD','ABCD','ABCD'] (with blocksize=3)
Used for keylength ciphers like Vineger,
too thread every nth letter as their own rot-cipher.
Arguments:
datastr     -- string
blocksize   -- integer (keylength)"""
    letters = [''] * blocksize
    datastr = clean_datastr(datastr)
    for i,char in enumerate(datastr):
        letters[i % blocksize] += char
    return letters

# Sort list of tuples by value in reverse order (high-low)
def sort_by_value(tuples,reverse=True):
    return sorted(tuples, key=lambda k: k[1], reverse=reverse)

# Simple Caesar Cipher per character
def rot(char, rotate):
    nr = ord(char)
    # Uppercase letters
    if nr > 64 and nr < 91:
        nr -= 65
        nr += rotate
        nr %= 26
        nr += 65
    # Lowercase letters
    if nr > 96 and nr < 123:
        nr -= 97
        nr += rotate
        nr %= 26
        nr += 97
    return chr(nr)

# Indices of given substring in datastring
def find_indc(datastr, substr, indices=[]):
    try:
        indx = datastr.index(substr)
    except:
        return
    if len(indices) > 0:
        indices.append(indices[-1]+indx+1)
    else:
        indices.append(indx)
    find_indc(datastr[indx+1:], substr, indices)
    return indices

# Occurence of each block/group of characters
def block_freq(datastr, blksize=1, shift=True):
    datastr = clean_datastr(datastr)
    diction = {}
    blocks = group(datastr, blksize, shift)
    for sub in blocks:
        if sub not in diction:
            diction[sub] = blocks.count(sub)
    return sort_by_value(diction.items())

# Print two dimensional list in nice columns
def column_print(data, head=[], nr_of_rows=0, max_width=79):
    # print out all the data
    if not nr_of_rows:
        nr_of_rows = len(data)
    # print out the head first
    if head:
        data = [head] + data
        nr_of_rows += 1
    # calculate the column width for each column
    column_width = [max(map(len,map(str,col))) + 2 for col in zip(*data)]
    # Factor in the max-width
    while sum(column_width) > max_width:
        i = column_width.index(max(column_width))
        column_width[i] -= 1
    def adjust(string,length):
        if len(string) < length:
            return string.ljust(length)
        else:
            # Padding is reduced too 1
            return string[:length-3] + ".. "
    for row in data[:nr_of_rows]:
        print("".join([adjust(str(attr),column_width[i])
                for i, attr in enumerate(row)]))

# ANALYSE
# ---------------------------------------------------------
# Chi-squared analyses
# Simularity of two probability distributions
# Comparing freq_analyses with dictionaries
def chi_squared(freq_an):
    for i in range(1,len(freq_an)):
        if len(freq_an[i][0]) != len(freq_an[i-1][0]):
            n = 0
            break
        else:
            n = len(freq_an[i][0])
    dictio = get_ngram(n)
    total = sum(f[1] for f in freq_an)
    chi = 0
    for [l,c] in freq_an:
        try:
            e = total * dictio[l]
        except:
            e = 0.01
        chi += (c-e)**2/e
    return chi

# IC of given keylength
def IC_analyses(datastr, keylength=1):
    datastr = clean_datastr(datastr)
    if keylength > len(datastr):
        return (0.0,0.0)
    blocks = [''] * keylength
    ics = []
    for i in range(keylength):
        blocks[i] = "".join(
            [datastr[k] for k in range(i,len(datastr),keylength)]
       )
    for b in blocks:
        if len(b) >= keylength:
            ics.append(IC(b))
    if len(ics) > 1:
        return (np.mean(ics),np.std(ics))
    elif len(ics) == 1:
        return (ics[0],0.0)
    else:
        return (0.0,0.0)

# Return average occurence of specific block
# Sorted by occurence
def block_freq_analyses(datastr, blksize=1, shift=True):
    freq = block_freq(datastr, blksize, shift)
    total = len(datastr)
    return [(f[0], float(f[1]*len(f[0]))/total) for f in freq]

# Try to detect if the text is English
def score_english(text):
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
# Caesar rotation value
# returns: (ROT,chi-squared,text)
def find_ROT(datastr):
    result = []
    for i in range(26):
        text = caesar_decrypt(datastr, i)
        result.append(
           (i,
            chi_squared(block_freq(text.upper())),
            text)
        )
    return sort_by_value(result, reverse=False)

# Alphabetic cipher compose keys
# Given two alphabets
def alphabetic_compose_key(from_alpha, to_alpha):
    EN_ALPHABET = "ETAONISRHLDUCMFWGPYBVKXJQZ"
    key = [''] * 26
    from_alpha = from_alpha.upper()
    to_alpha = to_alpha.upper()
    for i in range(len(key)):
        try:
            key[ord(from_alpha[i])-65] = to_alpha[i]
        except:
            break
    # fill the gaps...
    while True:
        try:
            indx = key.index('')
        except:
            break
        else:
            for c in EN_ALPHABET:
                if c not in key:
                    key[indx] = c
                    break
    return "".join(key)

# Compose possible key's from one-letter frequency analyses
def alphabetic_keys(freq_an):
    # TODO
    l


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
    for p in product(*nth_rot):
        key = ''
        total_ic = 0
        for rot,ic in p:
            key += chr(rot+65)
            total_ic += ic
        data.append((
                     key,
                     float(total_ic)/keylength,
                     vinegere_decrypt(datastr, key)
                    ))
        if not interactive:
            break
        if len(data) > keylength*2:
            break
    return sort_by_value(data,reverse=False)


# ENCRYPT/DECRYPT
# ---------------------------------------------------------
# Harder encryption
# Removes punctuations and whitespace
# Make uppercase, and group by 5 letters
def encrypt_hard(datastr):
    remove = st.punctuation + st.whitespace
    datastr = re.sub('['+remove+']','',datastr)
    # for p in remove:
    #     datastr = "".join(datastr.split(p))
    return " ".join(group(datastr.upper(), 5))

# Vineger cipher
def vinegere(datastr, key, fn):
    result = ''
    datastr = clean_datastr(datastr)
    illegal = st.punctuation
    for i in range(len(datastr)):
        k = key[i % len(key)]
        if k in illegal:
            print("Illegal char '{}' found in decoding key!".format(k))
            exit(2)
        else:
            result += rot(datastr[i], fn(ord(k))).lower()
    return result

def vinegere_encrypt(datastr, key):
    remove = st.punctuation + st.whitespace
    datastr = re.sub('['+remove+']','',datastr)
    return vinegere(datastr, key, lambda k: (k - 65))

def vinegere_decrypt(datastr, key):
    return vinegere(datastr, key, lambda k: 26 - (k - 65))

# Mono aplhabetic substitution encryption
def alphabetic_encrypt(datastr, key):
    if len(key) != 26 or len(set(key)) != 26:
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
    if key != None:
        try:
            key = int(key)
        except:
            cipher = "vinegere"
        else:
            cipher = "caesar"
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
    parser = argparse.ArgumentParser(description='A commandline deCipher tool.',
            epilog="Created by S. Thewessen")
    parser.add_argument('files', metavar='file',nargs='+',
            help='Input file(s) too use for encryption/decryption.')
    parser.add_argument('-e','--encode', metavar='encode', action='store_const',const=True,default=False,
            help='Run this program too encode the input (default: decode)')
    parser.add_argument('-i','--interactive', metavar='interactive', action='store_const',const=True,default=False,
            help='Interactive mode.')
    parser.add_argument('-k','--key', metavar='K', nargs='?',
            help='The key too use for the cipher. If the key is an integer, a basic Caesar Cipher is used.')
    parser.add_argument('-l','--length', metavar='N', nargs='?', type=int,
            help='The length N of the key as an integer (Vinegere)')
    parser.add_argument('-c','--cipher', choices=['caesar','alphabetic','vinegere'],
            help='Force a specific cipher too use.')
    parser.add_argument('-F','--frequency-analyses', metavar='N', nargs='?',
            dest='freq',
            const=True,type=int,
            default=0,
            help='Give the frequency analyses of block size N of the given data.')
    args = parser.parse_args()

    key = None
    data = []
    # # Get the correct key and data
    # if args.key == None and args.length == None and len(args.files) > 1:
    #     try:
    #         f = open(args.files[0])
    #         f.close()
    #     except:
    #         args.key = args.files[0]
    #         args.files = args.data[1:]
    # Some error messages for given key and length
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
        ss = re.findall(r'[^,^(^)^ ]*',str(args))
        for s in ss[1:]:
            if s != '':
                print(s)
        print('')
    # Setup the right function to use
    def fn(dstr):
        if args.cipher == "caesar":
            if args.key:
                try:
                    args.key = int(args.key)
                except:
                    print("You need an integer key to use with a rotation cipher!")
                    exit(2)
            if args.encode:
                if not args.key:
                    args.key = 13
                result = caesar_encrypt(dstr, args.key)
                return encrypt_hard(result)
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
        if args.cipher == "alphabetic":
            if args.key != None:
                if args.encode:
                    result = alphabetic_encrypt(dstr, args.key)
                    return encrypt_hard(result)
                else:
                    return alphabetic_decrypt(dstr, args.key)
            else:
                # TODO: Find the key!!
                freq = block_freq(dstr,3)
                print(chi_squared(freq))
                # column_print(chi_squared(freq),head=['block','chi'])
        if args.cipher == "vinegere":
            if args.key != None:
                if args.encode:
                    result = vinegere_encrypt(dstr, args.key)
                    return encrypt_hard(result)
                else:
                    return vinegere_decrypt(dstr, args.key)
            else:
                if args.encode:
                    print("Give an alphabetic key too use for encoding:")
                    args.key = input()
                    result = vinegere_encrypt(dstr, args.key)
                    return encrypt_hard(result)
                else:
                    max_number_keys = 1
                    if args.interactive:
                        start = time.time()
                        max_number_keys = 20
                    if not args.length:
                        key_ls = find_vin_keylength(dstr)
                        args.length = np.gcd.reduce([kl[0] for kl in key_ls])
                        if args.interactive:
                            column_print(key_ls, head=[
                                                'KL',
                                                'IC-analyses (mean)',
                                                'IC-analyses (standard deviation)'
                                               ])
                            print("The keylength is possibly {}.\n"\
                                    .format(args.length))
                    result = gen_vin_keys(dstr,args.length,
                                          interactive=args.interactive)
                    (args.key, score, text) = result[0]
                    if args.interactive:
                        column_print(result, head=['key','chi-squared (mean)','text'])
                        print("The key {} was used with an average chi-squared score of {}."\
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
            freq = block_freq_analyses(dstr,args.freq)
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

# UNUSED
# ---------------------------------------------------------
# Calculate the factors of any integer greater than 2
def calc_factors(integer):
    fact = []
    if integer < 2:
        return fact
    for i in range(2,integer + 1):
        if(integer % i == 0):
            fact.append(i)
    return fact

# Calculate the gap (and fractors) between substrings of a datastring
# You may also give it the block_freq_analyses list
def keylength_analyses(datastr, substrs):
    diffs = []
    factors = []
    result = []
    for substr in substrs:
        if type(substr[1]) == list:
            f = substr[1]
        else:
            f = find_indc(clean_datastr(datastr), substr)
        diffs += [f[i+1] - f[i] - 1 for i in range(0,len(f)-1,2)]
    for d in diffs:
        factors += calc_factors(d)

    result = sorted(set(factors), 
                     key=lambda k: factors.count(k),
                     reverse=True)
    return result

