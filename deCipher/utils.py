#!/usr/bin/python3

import re
import string as st
import numpy as np

# PARAMS
# ---------------------------------------------------------
# files
DICTIONARY = "./dictionaries/dictionary.txt"
WORDS = "./dictionaries/words"
MONOGRAMS = "./dictionaries/monograms"
BIGRAMS = "./dictionaries/bigrams"
TRIGRAMS = "./dictionaries/trigrams"
QUADGRAMS = "./dictionaries/quadgrams"

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
        print("Reading from file {}...".format(sources[N]))
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
indention"""
    return re.sub(' +', ' ', message).strip()


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
"AAABBBCCCDDDD" => 'ABCDD','ABCD','ABCD' (with blocksize=3)
Used for keylength ciphers like Vineger,
too thread every nth letter as their own rot-cipher.
Arguments:
datastr     -- string
blocksize   -- integer (keylength)"""
    datastr = clean_datastr(datastr)
    for i in range(blocksize):
        nthletters = [datastr[c] for c in range(i, len(datastr), blocksize)]
        yield "".join(nthletters)


def sort_by_value(tuples, reverse=True):
    """Sort list of tuples by their second element (used alot)"""
    return sorted(tuples, key=lambda k: k[1], reverse=reverse)


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
            return string[:length-3] + ".. "

    for row in data[:nr_of_rows]:
        print("".join([adjust(str(attr), column_width[i])
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


def IC_analyses(datastr, keylength=1):
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
            t = "".join(t.split(w))
        if len(t) == 0:
            break
    return float(len(text) - len(t)) / len(text) * 100
