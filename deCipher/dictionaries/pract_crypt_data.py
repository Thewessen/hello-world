#!/usr/bin/python

LANGUAGES = [
            'english',
            'danish',
            'finnish',
            'french',
            'german',
            'icelandic',
            'polish',
            'spanish',
            'swedish'
            ]

DATA = [
        'bigrams',
        'monograms',
        'quadgrams',
        'trigrams',
        'words'
        ]

for language in LANGUAGES:
    for ngram in DATA:
        input_file = language + '/' + language + '_' + ngram + '.txt'
        output_file = '../' + language[:2].upper() + "/" + ngram
        try:
            data_in = open(input_file)
        except:
            continue
        else:
            data_out = open(output_file,"w+")
            lines = data_in.read().splitlines()
            total = 0

            for l in lines:
                count = int(l.split(' ')[1])
                total += count

            tupples = [(l[0],float(l[1])/total) for l in [d.split(' ') for d in lines]]
            for t in tupples:
                data_out.write(t[0] + ' ' + str(t[1]) + '\n')
            data_in.close()
            data_out.close()
