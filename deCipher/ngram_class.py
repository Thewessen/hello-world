#!/usr/bin/python3

class ngram:
    def __init__(self):
        self._words = None
        self._monograms = None
        self._bigrams = None
        self._trigrams = None
        self._quadgrams = None

    def get_words(self):
        if not self._words:
            source = './dictionaries/words'
            with open(source) as fl:
                data = fl.read().splitlines()
            result = [d.split(' ') for d in data]
            dictio = {}
            for a,b in result:
                dictio[a.strip()] = float(b)
            self._words = dictio
        return self._words

    def get_monograms(self):
        if not self._monograms:
            source = './dictionaries/monograms'
            with open(source) as fl:
                data = fl.read().splitlines()
            result = [d.split(' ') for d in data]
            dictio = {}
            for a,b in result:
                dictio[a.strip()] = float(b)
            self._monograms = dictio
        return self._monograms

    def get_bigrams(self):
        if not self._bigrams:
            source = './dictionaries/bigrams'
            with open(source) as fl:
                data = fl.read().splitlines()
            result = [d.split(' ') for d in data]
            dictio = {}
            for a,b in result:
                dictio[a.strip()] = float(b)
            self._bigrams = dictio
        return self._bigrams

    def get_trigrams(self):
        if not self._trigrams:
            source = './dictionaries/trigrams'
            with open(source) as fl:
                data = fl.read().splitlines()
            result = [d.split(' ') for d in data]
            dictio = {}
            for a,b in result:
                dictio[a.strip()] = float(b)
            self._trigrams = dictio
        return self._trigrams

    def get_quadgrams(self):
        if not self._quadgrams:
            source = './dictionaries/quadgrams'
            with open(source) as fl:
                data = fl.read().splitlines()
            result = [d.split(' ') for d in data]
            dictio = {}
            for a,b in result:
                dictio[a.strip()] = float(b)
            self._quadgrams = dictio
        return self._quadgrams

    def set_ngram(self,word):
        print("Property may not be set!")

    words = property(get_words,set_ngram)
    monograms = property(get_monograms,set_ngram)
    bigrams = property(get_bigrams,set_ngram)
    trigrams = property(get_trigrams,set_ngram)
    quadgrams = property(get_quadgrams,set_ngram)
