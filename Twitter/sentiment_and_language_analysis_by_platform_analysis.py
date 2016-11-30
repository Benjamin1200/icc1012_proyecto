import time
import sys

# Analysis
with open("sentiment_and_language_analysis_by_platform_summary.txt", 'r') as fo:
    fo.readline()
    pos = []
    neg = []
    neu = []
    chars_to_remove = [',', '[', ']', '"']
    j = 4
    while True:
        i = fo.readline()
        line = i.translate(None, ''.join(chars_to_remove))
        line = line.split()
        if len(line) == 0:
            j -= 1
            if j == 0:
                break
            fo.readline()
            fo.readline()
        else:
            if line[1] == "pos":
                pos.append([line[0], int(line[2])])
            elif line[1] == "neg":
                neg.append([line[0], int(line[2])])
            else:
                neu.append([line[0], int(line[2])])

    total_pos = 0
    total_neg = 0
    total_neu = 0
    for language in pos:
        total_pos += language[1]
    for language in neg:
        total_neg += language[1]
    for language in neu:
        total_neu += language[1]

    pos_languages = {}
    neu_languages = {}
    neg_languages = {}
    for language in pos:
        try:
            pos_languages[language[0]] += language[1]
        except:
            pos_languages[language[0]] = language[1]
    for language in neu:
        try:
            neu_languages[language[0]] += language[1]
        except:
            neu_languages[language[0]] = language[1]
    for language in neg:
        try:
            neg_languages[language[0]] += language[1]
        except:
            neg_languages[language[0]] = language[1]

    for language in pos_languages.items():
        print "The percentage of positive sentiment in the {} language against the total of positive tweets in all the platforms: {}%".format(language[0], round(float(language[1])/total_pos*100, 2))
    for language in neu_languages.items():
        print "The percentage of neutral sentiment in the {} language against the total of neutral tweets in all the platforms: {}%".format(language[0], round(float(language[1])/total_neu*100, 2))
    for language in neg_languages.items():
        print "The percentage of negative sentiment in the {} language against the total of negative tweets in all the platforms: {}%".format(language[0], round(float(language[1])/total_neg*100, 2))

