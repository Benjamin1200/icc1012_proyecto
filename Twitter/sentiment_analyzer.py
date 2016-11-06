from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json
import sys


def init_classifier():
    n_instances = 100
    subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
    obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]

    train_subj_docs = subj_docs[:80]
    test_subj_docs = subj_docs[80:100]
    train_obj_docs = obj_docs[:80]
    test_obj_docs = obj_docs[80:100]
    training_docs = train_subj_docs + train_obj_docs
    testing_docs = test_subj_docs + test_obj_docs

    sentim_analyzer = SentimentAnalyzer()
    all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])
    unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
    sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)
    training_set = sentim_analyzer.apply_features(training_docs)
    test_set = sentim_analyzer.apply_features(testing_docs)
    trainer = NaiveBayesClassifier.train
    classifier = sentim_analyzer.train(trainer, training_set)
    sid = SentimentIntensityAnalyzer()
    return sid


def classify_file(_file, sid):
    _data = open(_file, 'r')
    open(_file[:-5] + "_classified.data", 'w').close()
    _output = open(_file[:-5] + "_classified.data", 'a')
    for line in _data.readlines():
        record = json.loads(line)
        ss = sid.polarity_scores(record['text'].encode('utf-8'))
        if ss['compound'] < 0:
            classification = "neg"
        elif ss['compound'] == 0:
            classification = "neu"
        else:
            classification = "pos"
        try:
            record.update({'classification': classification})
            _output.write(json.dumps(record, sort_keys=True) + "\n")
        except:
            # Should not happen.
            print "WTF!"
    _data.close()
    _output.close()
    return _output.name

if __name__ == '__main__':
    pass
