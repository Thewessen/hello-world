#!/usr/bin/python3

# import time
import re
import string as st
import sys
from itertools import product

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
    from_alpha = clean_datastr(from_alpha)
    to_alpha = clean_datastr(to_alpha)
    for i in range(len(from_alpha)):
        key[ord(from_alpha[i])-65] = to_alpha[i]
    # fill the gaps...
    for i, (k, EN) in enumerate(zip(key, EN_ALPHABET)):
        if k == '':
            key[i] = EN
    return "".join(key)


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


def partial_substitute(datastr, mapping):
    datastr = clean_datastr(datastr)
    for k, v in mapping.items():
        datastr = re.sub(k, v.lower(), datastr)
    return datastr


def create_mapping(from_word, too_word):
    dictio = {}
    fr = list(from_word)
    to = list(too_word)
    for f, t in zip(fr, to):
        dictio[f] = t
    return dictio


def create_pattern_word(datastr, mapping={}):
    done = ''
    pattern = []
    for i in range(len(datastr)):
        if datastr[i] in mapping.keys():
            pattern.append(mapping[datastr[i]])
        elif datastr[i] in done:
            pattern.append(done.index(datastr[i]))
        else:
            done += datastr[i]
            pattern.append(len(done)-1)
    return pattern


def create_pattern_dictio(datastr, mapping={}):
    done = ''
    pattern = []
    for i in range(len(datastr)):
        if datastr[i] in mapping.values():
            pattern.append(datastr[i])
        elif datastr[i] in done:
            pattern.append(done.index(datastr[i]))
        else:
            done += datastr[i]
            pattern.append(len(done)-1)
    return pattern


def match_pattern_dictionary(pattern, mapping={}):
    # dictio = get_ngram(0)
    with open(DICTIONARY) as di:
        dictio = di.read().splitlines()
    for k in dictio:
        if len(k) != len(pattern):
            continue
        p = create_pattern_dictio(k, mapping)
        match = True
        for p1, p2 in zip(pattern, p):
            if type(p1) != type(p2) or p1 != p2:
                match = False
                break
        if match:
            yield k


def dictionary_attack(datastr, mapping={}):
    # max word length is 15
    if len(datastr) < 15:
        rng = range(len(datastr), 1, -1)
    else:
        rng = range(15, 1, -1)
    matches = []
    for i in rng:
        pattern = create_pattern_word(datastr[:i], mapping)
        matches = list(match_pattern_dictionary(pattern))
        if len(matches) == 0:
            continue
        elif len(datastr) == i:
            return matches
        else:
            for m in matches:
                new_mapping = create_mapping(datastr[:i], m)
                new_mapping.update(mapping)
                print(new_mapping)
                new_matches = dictionary_attack(datastr[i:], new_mapping)
                if len(new_matches) > 0:
                    return list(product(matches, new_matches))
    return []


if __name__ == "__main__":
    with open(sys.argv[1]) as fl:
        text = fl.read().splitlines()
    text = clean_datastr(text[0])
    pattern = create_pattern_word(text[:12])
    print(len(set(text[:12])))
    print(pattern)
    print(list(match_pattern_dictionary(pattern)))
