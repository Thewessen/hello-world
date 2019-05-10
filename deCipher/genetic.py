#!/usr/bin/python3
# A cenetic algorithm for finding the key
# in a mono-alphabetic substitution cipher

import string
import sys
import re
from random import randint
from random import shuffle
from random import choice

MAX_GENERATIONS = 1000   # Max number of generations
MAX_BEST_KEYS = 20
POPULATION_SIZE = 20    # Max population size
TOP_POPULATION = 4      # Top population size
CROSSOVER_COUNT = 2     # Number of times to apply crossover
MUTATION_COUNT = 1      # Number of times to apply mutation
CHARS = string.ascii_uppercase
DICTIONARY = './dictionaries/dictionary.txt'
WORDS = "./dictionaries/words"
MONOGRAMS = "./dictionaries/monograms"
BIGRAMS = "./dictionaries/bigrams"
TRIGRAMS = "./dictionaries/trigrams"
QUADGRAMS = "./dictionaries/quadgrams"

NGRAMS = {0: None,
          1: None,
          2: None,
          3: None,
          4: None}


# TOOLS
# ---------------------------------------------------------
def get_ngram(N=1):
    """Returns corresponding ngram as an dictionary object,  e.g.:
bigram = {
    'TH':   0.0270569804001
    'HE':   0.0232854497343
    'IN':   0.0202755339125
    ...
    string: float
}

Arguments:
N       -- ngram integer,  choices:
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
        for a,  b in result:
            NGRAMS[N][a.strip()] = float(b)
    return NGRAMS[N]


# Sort list of tuples by value in reverse order (high-low)
def sort_by_value(tuples, reverse=True):
    return sorted(tuples,  key=lambda k: k[1],  reverse=reverse)


# Print two dimensional list in nice columns
def column_print(data,  head=[],  nr_of_rows=0,  max_width=79):
    # print(out all the data)
    if not nr_of_rows:
        nr_of_rows = len(data)
    # print(out the head first)
    if head:
        data = [head] + data
        nr_of_rows += 1
    # calculate the column width for each column
    column_width = [max(map(len, map(str, col))) + 2 for col in zip(*data)]
    # Factor in the max-width
    while sum(column_width) > max_width:
        i = column_width.index(max(column_width))
        column_width[i] -= 1

    def adjust(string, length):
        if len(string) < length:
            return string.ljust(length)
        else:
            # Padding is reduced too 1
            return string[:length-3] + ".. "
    for row in data[:nr_of_rows]:
        print("".join([adjust(str(attr), column_width[i])
              for i, attr in enumerate(row)]))


# Make sure datastrinc is all uppercase
# and contains no blank chars
def clean_datastr(datastr):
    if datastr.find(' ') or datastr.find('\n') or datastr.find('\r'):
        datastr = "".join(datastr.split())
    if not datastr.isupper():
        datastr = datastr.upper()
    return datastr


# Create block-groups of characters
def block_group(datastr,  blksize):
    datastr = clean_datastr(datastr)
    return [datastr[i:i+blksize] for i in range(0, len(datastr), blksize)]


# Create shift-groups of characters
def shift_group(datastr,  blksize):
    datastr = clean_datastr(datastr)
    return [datastr[i:i+blksize] for i in range(len(datastr)-blksize+1)]


def block_freq(datastr,  blksize=1,  shift=True):
    datastr = clean_datastr(datastr)
    diction = {}
    if shift:
        blocks = shift_group(datastr,  blksize)
    else:
        blocks = block_group(datastr,  blksize)
    for sub in blocks:
        if sub not in diction:
            diction[sub] = blocks.count(sub)
    return diction.items()


def block_freq_analyses(datastr,  blksize=1,  shift=True):
    freq = block_freq(datastr,  blksize,  shift)
    total = len(datastr)
    return [(f[0],  float(f[1]*len(f[0]))/total) for f in freq]


def initial_keys(encrypt):
    # monogram = [k for k, _ in sort_by_value(get_ngram().items())]
    # freq = [k for k, _ in sort_by_value(block_freq(encrypt))]
    # key = list(alphabetic_compose_key(freq, monogram))
    keys = []
    for i in range(POPULATION_SIZE):
        key = list(CHARS)
        shuffle(key)
        keys.append("".join(key))
    return keys


def alphabetic_encrypt(datastr,  key):
    if len(key) != 26 or len(set(key)) != 26:
        print("Not a complete alhabet found in mono alphabetic cipher key: "
              + str(key))
        exit(2)
    key = key.upper()
    skip = string.punctuation + string.whitespace + string.digits
    result = ''
    for c in datastr:
        if c in skip:
            result += c
        else:
            result += key[ord(c.upper()) - 65].lower()
    return result


# Alphabetic cipher compose keys
# Given two alphabets
def alphabetic_compose_key(from_alpha,  to_alpha):
    EN_ALPHABET = "ETAONISRHLDUCMFWGPYBVKXJQZ"
    key = [''] * 26
    # from_alpha = from_alpha.upper()
    # to_alpha = to_alpha.upper()
    for i in range(len(key)):
        try:
            key[ord(from_alpha[i])-65] = to_alpha[i]
        except IndexError:
            break
    # fill the gaps...
    while True:
        try:
            indx = key.index('')
        except ValueError:
            break
        else:
            for c in EN_ALPHABET:
                if c not in key:
                    key[indx] = c
                    break
    return "".join(key)


# Mono aplhabetic substitution decryption
def alphabetic_decrypt(datastr,  key):
    decr_key = alphabetic_compose_key(key,  string.ascii_uppercase)
    return alphabetic_encrypt(datastr,  decr_key)


# def fitness(text):
#     # Get all the words from the DICTIONARY file
#     with open(DICTIONARY) as f:
#         english_words = f.read().split()
#     # and make sorted list,  largest word first
#     english_words.sort(key = lambda s: len(s), reverse=True)
#     # Calculate a score based on the remaining text
#     t = clean_datastr(text)
#     for w in english_words:
#         if len(w) > len(t):
#             continue
#         if w in t:
#             t = "".join(t.split(w))
#         if len(t) == 0:
#             break
#     return float(len(text) - len(t)) / len(text) * 100
def fitness(text):
    chi = 0
    for i in range(1, 4):
        freq_an = block_freq(text, i)
        dictio = get_ngram(i)
        total = sum(f[1] for f in freq_an)
        for [l, c] in freq_an:
            try:
                e = total * dictio[l]
            except KeyError:
                e = 0.01
            chi += (c-e)**2/e
    return chi
# def fitness(text):
#     a = b = c = 1
#     scores = []
#     for i in range(1, 4):
#         freq = sorted(block_freq_analyses(text, i))
#         ngram = get_ngram(i)
#         score = 0.0
#         for k, v in freq:
#             try:
#                 score += abs(ngram[k]-v)
#             except KeyError:
#                 score += v
#         scores.append(score)
#     return a*scores[0] + b*scores[1] + c*scores[2]

# def stochasticly_pick(keys, pick):
#     picks = []
#     r = randint(0, len(keys))
#     step = len(keys)/pick
#     for i in range(pick):
#         picks.append(keys[(r+step*i)%len(keys)])
#     return picks


def random_pick(selection, N=2):
    s = list(selection)
    selected = []
    for i in range(N):
        selected += [s.pop(randint(0, len(s)-1))]
    return selected


def form_pairs(selection):
    select = list(selection)
    pairs = []
    while len(select) > 1:
        parent1 = select.pop(randint(0, len(select))-1)
        parent2 = select.pop(randint(0, len(select))-1)
        pairs.append([parent1, parent2])
    return pairs


def fill(gen, complete):
    for g in complete:
        if g not in gen:
            gen[gen.index('')] = g
    return gen


# Apply crossover
# to generate two children
def crossover(parents):
    parent1 = list(parents[0])
    parent2 = list(parents[1])
    r = randint(0, len(parent1))
    parent11 = parent1[:r]
    parent12 = parent1[r:]
    parent21 = parent2[:r]
    parent22 = parent2[r:]
    child1 = [''] * len(parent12)
    child2 = [''] * len(parent22)
    # crossover
    for i, (p12, p22) in enumerate(zip(parent12, parent22)):
        if p12 not in parent21:
            child2[i] = p12
        if p22 not in parent11:
            child1[i] = p22
    child1 = fill(parent11 + child1, string.ascii_uppercase)
    child2 = fill(parent21 + child2, string.ascii_uppercase)
    return ["".join(child1), "".join(child2)]
    # # fill
    # for g in string.ascii_uppercase:
    #     if g not in child1:
    #         child1[child1.index('')] = g
    #     if g not in child2:
    #         child2[child2.index('')] = g


# Pick two parents randomly from selection
# Mutatate them,
# to generate two children
def mutation(parents):
    parent1 = list(parents[0])
    parent2 = list(parents[1])
    gen = [randint(0, 1) for _ in range(26)]
    child1 = [''] * 26
    child2 = [''] * 26
    # mutation
    for i, (g, p1, p2) in enumerate(zip(gen, parent1, parent2)):
        if g:
            child1[i] = p1
        else:
            child2[i] = p2
    # fill
    child1 = fill(child1, parent2)
    child2 = fill(child2, parent1)
    # for g in parent1:
    #     if g not in child2:
    #         child2[child2.index('')] = g
    # for g in parent2:
    #     if g not in child1:
    #         child1[child1.index('')] = g
    return ["".join(child1), "".join(child2)]


def swap_gen(child, gen, repl):
    s = gen + repl
    return re.sub(
        r'(.*)([%s])(.*)([%s])(.*)' % (s, s),
        r'\1\4\3\2\5',
        child
    )


def genetic(population, environment):
    while True:
        # Sort population by fittest
        fit = [(person, fitness(alphabetic_decrypt(environment, person)))
               for person in population]
        fit.sort(key=lambda k: k[1])
        # Keep strongest
        population = [k for k, _ in fit][:TOP_POPULATION]
        while len(population) < POPULATION_SIZE:
            # children = crossover(random_pick(population))
            # if len(population) % 4 == 0:
            #     children = mutation(children)
            # population += children
            p1, p2 = random_pick(population)
            for i in range(CROSSOVER_COUNT):
                char = choice(CHARS)
                indx = ord(char)-65
                child = swap_gen(p1, char, p2[indx])
            for i in range(MUTATION_COUNT):
                char = choice(CHARS)
                repl = choice(CHARS)
                child = swap_gen(child, char, repl)
            population.append(child)
        yield population


def main():
    with open(sys.argv[1]) as fl:
        text = fl.read()
    keys = initial_keys(text)
    generation = 0
    population = genetic(keys, text)
    best_key = ''
    prt = []
    best_keys = 0
    while generation < MAX_GENERATIONS and best_keys < MAX_BEST_KEYS:
        keys = next(population)
        new_best_key = keys[0]
        if new_best_key == best_key:
            best_keys += 1
        else:
            best_key = new_best_key
            best_keys = 0
        prt.append(['generation'+str(generation+1)+':'] + keys)
        if generation % 4 == 3:
            z = list(zip(*prt))
            column_print(z, max_width=120)
            print('\n')
            prt = []
        generation += 1

    fit = [(key, fitness(alphabetic_decrypt(text, key)))
           for key in keys]
    fit.sort(key=lambda k: k[1])
    column_print(fit, head=['recent population', 'score'])
    print(fitness(alphabetic_decrypt(text, best_key)))
    print(alphabetic_decrypt(text, best_key))


if __name__ == '__main__':
    # key: FIQWRTNKZLMBYCHSEXVPGUJDOA
    # file: aplhabetic/encrypted.txt
    # plain: plain/plaintext.txt
    # chi-squared(1): 109.3
    # chi-squared(1-4): 49525.86
    # chi-squared(3): 15272.4187
    # chi-squared(4): 129903.5196
    # score_english: 97.8177%
    # main()
    with open(sys.argv[1]) as fl:
        encr = fl.read()
    encr = clean_datastr(encr)
    print(encr)
    # print(decr)
    print(fitness(encr))
    # keys = initial_keys(encr)
    # key = 'FIQWRTNKZLMBYCHSEXVPGUJDOA'
    # key = CHARS[19:] + CHARS[:19]
    # decr = alphabetic_decrypt(encr, key)
    # print(decr)
    # print(fitness(decr))
    # print(keys)
    # print(swap_gen('FWZXIKCJPANRTYBOQSGDHVLMUE', 'K', 'C'))
    # print(random_pick(keys))
    # selection = random_pick(keys, 10)
    # parents = random_pick(selection)
    # print(crossover(parents))

    # parents:
    # - Keep 20% (2 best keys)
    # - Stochasticly select 8 more keys
    # - apply crossover (10 more children)
    # - apply mutation of 0.02% (too children)
    # - apply replacement
