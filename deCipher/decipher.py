#!/usr/bin/python

import string as st
# .ascii_uppercase
# .punctuations
import numpy as np
# .mean
# .std (standard deviation)
import argparse

# PARAMS
# ---------------------------------------------------------
DICTIONARY = "dictionary.txt"

# TOOLS
# ---------------------------------------------------------
# Index of Coincidence
def IC(datastr):
    # Make sure the datastr is all upper and nonblank
    datastr = "".join(datastr.split())

    # Formula: IC = (n  * (n - 1))/(N * (N - 1))
    # With
    # n: occurence of letter from alphabet in string
    # N: total number of letters in string
    n = 0.0
    r = 0.0
    t = float(len(datastr))
    t = t * (t - 1)
    for c in st.ascii_uppercase:
        o = float(datastr.count(c))
        n += o * (o - 1)
    r = n / t
    return r

# Calculate the factors of any integer greater than 2
def calc_factors(integer):
    fact = []
    if integer < 2:
        return fact
    for i in range(2,integer + 1):
        if(integer % i == 0):
            fact.append(i)
    return fact

# Make sure printable text contains only UTF8 characters
# BRUTE METHOD
def clean_text(text):
    for c in text:
        if ord(c) > 126:
            text = "".join(text.split(c))
    return text

# Make sure datastring is all uppercase 
# and contains no blank chars
def clean_datastr(datastr):
    if datastr.find(' ') or datastr.find('\n') or datastr.find('\r'):
        datastr = "".join(datastr.split())
    if not datastr.isupper():
        datastr = datastr.upper()
    return datastr

# Create block-groups of characters
def block_group(datastr, blksize):
    datastr = clean_datastr(datastr)
    return [datastr[i:i+blksize] for i in range(0,len(datastr),blksize)]

# Create shift-groups of characters
def shift_group(datastr, blksize):
    datastr = clean_datastr(datastr)
    return [datastr[i:i+blksize] for i in range(len(datastr)-blksize+1)]

# Group every nth letter of each block 
# for treading as their own rot-cipher (vineger)
def nthletter_group(datastr, blksize):
    blocks = block_group(datastr, blksize)
    letters = {}
    for i in range(blksize):
        letters[i] = []
    for block in blocks:
        for i in range(len(block)):
            letters[i].append(block[i])
    return letters

# Sort list of tuples by value in reverse order (high-low)
def sort_by_value(tuples):
    return sorted(tuples, key=lambda k: k[1], reverse=True)

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
# Same as freq() when blksize=1 (default)
def block_freq(datastr, blksize=1, shift=True):
    datastr = clean_datastr(datastr)
    diction = {}
    if shift:
        blocks = shift_group(datastr, blksize)
    else:
        blocks = block_group(datastr, blksize)
    for sub in blocks:
        if sub not in diction:
            diction[sub] = blocks.count(sub)
    return sort_by_value(diction.items())

# Print two dimensional list in nice columns
def column_print(data, head=[], nr_of_rows=0):
    # print out all the data
    if nr_of_rows == 0:
        nr_of_rows = len(data)
    # print out the head first
    if len(head) != 0:
        data = [head] + data
    # calculate the column width
    column_width = max(len(str(attr)) for row in data for attr in row[:-1]) + 2
    # print
    for row in data[:nr_of_rows+1]:
        print "".join(str(attr).ljust(column_width) for attr in row)

# ANALYSE
# ---------------------------------------------------------
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
    total = float(len(datastr))
    return [(f[0], float(f[1]*len(f[0]))/total) for f in freq]

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
def find_ROT(datastr):
    result = []
    for i in range(26):
        text = caesar_decrypt(datastr, i)
        result.append((i, score_english(text.upper())))
    return sort_by_value(result)

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
    l

# ENCRYPT/DECRYPT
# ---------------------------------------------------------
# Vineger cipher
def vineger(datastr, key, fn):
    result = ''
    datastr = clean_datastr(datastr)
    illegal = st.punctuation + st.whitespace
    for i in range(len(datastr)):
        k = key[i % len(key)]
        if k == '?':
            result += datastr[i]
        elif k in illegal:
            print "Illegal char ' %s ' found in decoding key!" % k
            exit(2)
        else:
            result += rot(datastr[i], fn(ord(k))).lower()
    return result

def vineger_encrypt(datastr, key):
    return vineger(datastr, key, lambda k: (k - 65))

def vineger_decrypt(datastr, key):
    return vineger(datastr, key, lambda k: 26 - (k - 65))

# Mono aplhabetic substitution cipher
def alphabetic(datastr, key):
    if len(key) != 26 or len(set(key)) != 26:
        print "Not a complete alhabet found in mono alphabetic cipher key: " + str(key)
        exit(2)
    key = key.upper()
    skip = st.punctuation + st.whitespace
    result = ''
    for c in datastr:
        if c in skip:
            result += c
        else:
            result += key[ord(c.upper()) - 65].lower()
    return result
# Also removes punctuations and whitespace
# Makes text all uppercase
# And groups letters by 5
# To make it harder too decode
def alphabetic_encrypt(datastr, key):
    result = alphabetic(datastr, key)
    remove = st.punctuation + st.whitespace
    for p in remove:
        result = "".join(result.split(p))
    return " ".join(block_group(result.upper(), 5))

def alphabetic_decrypt(datastr, key):
    decr_key = alphabetic_compose_key(key, st.ascii_uppercase)
    return alphabetic(datastr, decr_key)

# Simple Caesar cipher (ROT#)
# Keeps punctuations and whitespace
def caesar_encrypt(datastr, rott):
    result = ''
    for c in datastr:
        result += rot(c, rott)
    return result

def caesar_decrypt(datastr, rott):
    return caesar_encrypt(datastr, 26-rott)

# DETECT ENCRYPTION
# ---------------------------------------------------------
def detect_cipher(datastr, key, interactive=False):
    cipher = ''
    if key != None:
        try:
            key = int(key)
        except:
            cipher = "vineger"
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
                cipher = "vineger"
        else:
            if interactive:
                print "Data string is too small to determin which cipher to use."
            cipher = "caesar"
    if interactive:
        print "Trying to use a %s cipher for the data string." % cipher
    return cipher

# MAIN PROGRAM
# ---------------------------------------------------------
# The program decipher.py reads from sys.args
def main():
    parser = argparse.ArgumentParser(description='A commandline deCipher tool.',
            epilog="Created by S. Thewessen")
    parser.add_argument('data', metavar='data',nargs='+',
            help='Input string(s) too use for encoding/decoding')
    parser.add_argument('-e','--encode', metavar='encode', action='store_const',const=True,default=False,
            help='Run this program too encode the input (default: decode)')
    parser.add_argument('-i','--interactive', metavar='interactive', action='store_const',const=True,default=False,
            help='Interactive mode.')
    parser.add_argument('-k','--key', metavar='key', nargs='?',
            help='The key too use for the cipher. If the key is an integer, a basic Caesar Cipher is used.')
    parser.add_argument('-l','--length', metavar='length', nargs='?', type=int,
            help='The length of the key')
    parser.add_argument('-c','--cipher', choices=['caesar','alphabetic','vineger'],
            help='Force a specific cipher too use.')
    args = parser.parse_args()

    key = None
    data = []
    # Get the correct key and data
    if args.key == None and args.length == None and len(args.data) > 1:
        try:
            f = open(args.data[0])
            f.close()
        except:
            args.key = args.data[0]
            args.data = args.data[1:]
    # Some error messages for given key and length
    if args.key and args.length:
        if len(args.key) != args.length:
            print "The given key '%s' and the given length %d are not the same. Please make sure they are or just ommit the length." % (args.key,args.length)
            exit(2)
    if args.encode and args.key == None:
        print "If you want to encrypt a given data string, you should give a key to encrypt with!"
        exit(2)
    if type(args.key) == str:
        for c in st.punctuation:
            if c in args.key and (args.encode or c != '?'):
                if args.encode:
                    e = 'encrypt'
                else:
                    e = 'decrypt'
                print "You can't %s a data string with a key containing '%s'! Key given: '%s'" % (e, c, args.key)
                exit(2)
    print args
    # Setup the right function to use
    def fn(dstr):
        if args.cipher == "caesar":
            if args.key != None:
                try:
                    args.key = int(args.key)
                except:
                    print "You need an integer key to use with a rotation cipher!"
                    exit(2)
            else:
                if args.encode:
                    return caesar_encrypt(datastr, args.key)
                else:
                    if args.key == None:
                        result = find_ROT(datastr)
                        if args.interactive:
                            column_print(result)
                        (args.key, score) = result[0]
                        print "Rotation %d is used with an english score of %.2f" % (args.key, score) + "%:"
                    return caesar_decrypt(datastr, args.key)
        if args.cipher == "alphabetic":
            if args.key != None:
                if args.encode:
                    return alphabetic_encrypt(datastr, args.key)
                else:
                    return alphabetic_decrypt(datastr, args.key)
            else:
                # TODO: Find the key!!
                freq = block_freq_analyses(datastr)
                EN = common_EN_letters()
                result = []
                for i in range(len(EN)):
                    if i < len(freq):
                        result.append(freq[i] + EN[i])
                    else:
                        result.append(('','') + EN[i])
                column_print(result)

    datastr = ''
    for d in args.data:
        try:
            f = open(d)
            datastr = f.read()
            f.close()
        except Exception as e:
            print e
            exit(2)
        datastr = datastr.strip()
        datastr = clean_text(datastr)
        if args.interactive: print "Input data given:\n" + datastr
        if args.cipher == None:
            if args.interactive: print "No specific cipher was given." 
            args.cipher = detect_cipher(datastr, args.key, args.interactive)
        output = fn(datastr)
        if args.interactive: print "Output:"
        print output


if __name__ == "__main__":
    # main()
    print score_english("HEYYOUTHERE")
    # print alphabetic_compose_key("SCQJUBGNDTZVWYKAEFOIHR", "SCQJUBGNDTZVWYKAEFOIHR")
    # column_print(common_EN_letters())
    # column_print(block_freq_analyses("HEYHEYHEYHEY"))

# UNUSED
# ---------------------------------------------------------
def print_poss_keylengths():
    print "possible key-lengths:" 
    keylengths = calc_poss_keylength([found1, found2, found3], [t[0] for t in total[1:4]])
    print keylengths

def convert_to_key(data, ii, oo, length):
    blocks = []
    keys = []
    for datastr in data:
        blocks += group(datastr, length)
    for b in blocks:
        if ii in b:
            key = ''
            start = b.index(ii)
            for i in range(start):
                key += '-'
            for j in range(len(ii)):
                key += chr((ord(oo[j]) - ord(ii[j]) - 1) % 26 + 65)
            for k in range(start+len(ii),length):
                key += '-'
            if key not in keys:
                keys.append(key)
    return keys

def try_find_key(data):
    # Find frequent occuring 3-blocks
    freq_an = freq_analyses(data, 3)
    common_encr = [e[0] for e in freq_an[:15]]
    keylengths = calc_poss_keylength(data, [t[0] for t in freq_an[1:4]])
    common_words = ['THE','AND','THA','ENT','ION','TIO','FOR','NDE','HAS','NCE','EDT','TIS','OFT','STH','MEN']
    poss_keys = []
    for n in keylengths[:4]:
        for e in common_encr:
            for w in common_words:
                poss_keys += convert_to_key(data, e, w, n)
    keys = set(poss_keys)
    for k in keys:
        score1 = score_english(vineger_decipher(found1, k))
        score2 = score_english(vineger_decipher(found2, k))
        score3 = score_english(vineger_decipher(found3, k))
        tsc = score1 + score2 + score3
        if tsc > 9:
            print "'%s' total score: " % k + str(tsc)
            print "found1 score: %s -------------------" % str(score1)
            print vineger_decipher(found1, k) 
            # print "found2 score: " + str(score2)
            print vineger_decipher(found2, k) 
            # print "found3 score: " + str(score3)
            print vineger_decipher(found3, k) 

def calc_keylengths(datastr):
    datastr = clean_datastr(datastr)
    blocks = []
    diffs = []
    result = {}
    for b in [datastr[i:i+3] for i in range(0,len(datastr)-3,1)]:
        if b not in blocks:
            blocks.append(b)
            frq = find_indc(datastr, b, [])
            if len(frq) > 2:
                frq.sort()
                for i in range(len(frq)-1):
                    for j in range(i+1,len(frq[i:])):
                        diffs.append(frq[j] - frq[i])
    fact = []
    for d in diffs:
        fact += calc_factors(d)
    uniq = set(fact)
    for u in uniq:
        result[u] = fact.count(u)
    result = sorted(result.items(),
                    key=lambda kv: (kv[1],kv[0]),
                    reverse=True) 
    print result

