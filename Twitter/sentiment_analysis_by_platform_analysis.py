import matplotlib.pyplot as plt
import numpy as np

class Platform:
    def __init__(self, name):
        self.name = name
        self.sentiments = {}

    def add_sentiment_amount(self, sentiment_list, sentiment_key):
        self.sentiments[sentiment_key] = sentiment_list

    def add_total_tweets(self, total):
        self.total = float(total)

    def print_sentiments_statistics(self):
        print "\n{}\n".format(self.name)
        for sentiment_list in self.sentiments.items():
            average_sentiment = np.average(sentiment_list[1])
            std_deviation_sentiment= np.std(sentiment_list[1], ddof=1)
            plt.boxplot(sentiment_list[1], vert=False)
            plt.title("{} - {} sentiment".format(self.name, sentiment_list[0]))
            plt.xlabel('Quantity')
            plt.show()
            total_sentiment = 0
            for i in sentiment_list[1]:
                total_sentiment += i
            print "The next information is for tweets with {} sentiment. The average was: {}. The standard deviation was: {}".format(sentiment_list[0], average_sentiment, std_deviation_sentiment)
            print "The percentage of {} sentiment tweets in this platform was: {}%".format(sentiment_list[0], round(total_sentiment/self.total*100, 2))


archivo = open("sentiment_analysis_by_platform_summary.txt")
archivo.readline()
archivo.readline()
pos = []
neg = []
neu = []
chars_to_remove = [',', '[', ']', '"']
while True:
    i = archivo.readline()
    line = i.translate(None, ''.join(chars_to_remove))
    line = line.split()
    if len(line) == 0:
        break
    if line[2] == "pos":
        pos.append([int(line[0]), int(line[1]), int(line[3])])
    elif line[2] == "neg":
        neg.append([int(line[0]), int(line[1]), int(line[3])])
    else:
        neu.append([int(line[0]), int(line[1]), int(line[3])])

# Statistics
nintendo = Platform("Nintendo")
negs_count = []
for row in neg:
    negs_count.append(row[2])
pos_count = []
for row in pos:
    pos_count.append(row[2])
neu_count = []
for row in neu:
    neu_count.append(row[2])

nintendo.add_sentiment_amount(negs_count, "negative")
nintendo.add_sentiment_amount(neu_count, "neutral")
nintendo.add_sentiment_amount(pos_count, "positive")
total = 0
for i in negs_count:
    total += i
for i in pos_count:
    total += i
for i in neu_count:
    total += i
nintendo.add_total_tweets(total)
nintendo.print_sentiments_statistics()

archivo.readline()
archivo.readline()
pos = []
neg = []
neu = []
chars_to_remove = [',', '[', ']', '"']
while True:
    i = archivo.readline()
    line = i.translate(None, ''.join(chars_to_remove))
    line = line.split()
    if len(line) == 0:
        break
    if line[2] == "pos":
        pos.append([int(line[0]), int(line[1]), int(line[3])])
    elif line[2] == "neg":
        neg.append([int(line[0]), int(line[1]), int(line[3])])
    else:
        neu.append([int(line[0]), int(line[1]), int(line[3])])

# Statistics
playstation = Platform("Playstation")
negs_count = []
for row in neg:
    negs_count.append(row[2])
pos_count = []
for row in pos:
    pos_count.append(row[2])
neu_count = []
for row in neu:
    neu_count.append(row[2])

playstation.add_sentiment_amount(negs_count, "negative")
playstation.add_sentiment_amount(neu_count, "neutral")
playstation.add_sentiment_amount(pos_count, "positive")
total = 0
for i in negs_count:
    total += i
for i in pos_count:
    total += i
for i in neu_count:
    total += i
playstation.add_total_tweets(total)
playstation.print_sentiments_statistics()

archivo.readline()
archivo.readline()
pos = []
neg = []
neu = []
chars_to_remove = [',', '[', ']', '"']
while True:
    i = archivo.readline()
    line = i.translate(None, ''.join(chars_to_remove))
    line = line.split()
    if len(line) == 0:
        break
    if line[2] == "pos":
        pos.append([int(line[0]), int(line[1]), int(line[3])])
    elif line[2] == "neg":
        neg.append([int(line[0]), int(line[1]), int(line[3])])
    else:
        neu.append([int(line[0]), int(line[1]), int(line[3])])

# Statistics
xbox = Platform("Xbox")
negs_count = []
for row in neg:
    negs_count.append(row[2])
pos_count = []
for row in pos:
    pos_count.append(row[2])
neu_count = []
for row in neu:
    neu_count.append(row[2])

xbox.add_sentiment_amount(negs_count, "negative")
xbox.add_sentiment_amount(neu_count, "neutral")
xbox.add_sentiment_amount(pos_count, "positive")
total = 0
for i in negs_count:
    total += i
for i in pos_count:
    total += i
for i in neu_count:
    total += i
xbox.add_total_tweets(total)
xbox.print_sentiments_statistics()

archivo.readline()
archivo.readline()
pos = []
neg = []
neu = []
chars_to_remove = [',', '[', ']', '"']
while True:
    i = archivo.readline()
    line = i.translate(None, ''.join(chars_to_remove))
    line = line.split()
    if len(line) == 0:
        break
    if line[2] == "pos":
        pos.append([int(line[0]), int(line[1]), int(line[3])])
    elif line[2] == "neg":
        neg.append([int(line[0]), int(line[1]), int(line[3])])
    else:
        neu.append([int(line[0]), int(line[1]), int(line[3])])

# Statistics
_else = Platform("Else")
negs_count = []
for row in neg:
    negs_count.append(row[2])
pos_count = []
for row in pos:
    pos_count.append(row[2])
neu_count = []
for row in neu:
    neu_count.append(row[2])

_else.add_sentiment_amount(negs_count, "negative")
_else.add_sentiment_amount(neu_count, "neutral")
_else.add_sentiment_amount(pos_count, "positive")
total = 0
for i in negs_count:
    total += i
for i in pos_count:
    total += i
for i in neu_count:
    total += i
_else.add_total_tweets(total)
_else.print_sentiments_statistics()
