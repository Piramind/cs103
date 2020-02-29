import math
import csv
import string
from typing import List, Dict
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
class NaiveBayesClassifier:

    def __init__(self, alpha = 1):
        self.alpha = alpha
        self.dictionary = {}
        self.labels = []
        self.l_chance = []

    def fit(self, X, y):
        """ Fit Naive Bayes classifier according to X, y. """
        X = [clean(x).lower() for x in X]
        self.labels = [label for label in set(y)]  
        self.l_chance = [y.count(label) / len(y) for label in self.labels] 
        for id, word_list in enumerate(X):
            word_list = word_list.split() 
            for word in word_list:
                if self.dictionary.get(word): 
                    self.dictionary[word][0][self.labels.index(y[id])] += 1  
                else:
                    self.dictionary.update({word: [[0 for label in self.labels], [0 for label in self.labels]]})
                    self.dictionary[word][0][self.labels.index(y[id])] += 1
        labels = [0 for label in self.labels]
        for id in range(len(labels)): 
            for word in self.dictionary:
                labels[id] += self.dictionary[word][0][id]
        for word in self.dictionary:
            for id in range(len(self.dictionary[word][1])):
                self.dictionary[word][1][id] = (self.alpha + self.dictionary[word][0][id]) / (
                            self.alpha * len(self.dictionary) + labels[id])

    def predict(self, X):
        """ Perform classification on an array of test vectors X. """
        # Вычисление класса по входящим данным
        X = [clean(x).lower() for x in X]
        y = []
        for word_list in X:
            chance_of_class = []
            word_list = word_list.split()
            for id in range(len(self.labels)):
                chance_label = math.log(self.l_chance[id])
                for word in word_list:
                    if self.dictionary.get(word):
                        chance_label += math.log(self.dictionary[word][1][id]) 
                chance_of_class.append(chance_label)
            y.append(self.labels[chance_of_class.index(max(chance_of_class))])
        return y

    def score(self, X_test, y_test):
        """ Returns the mean accuracy on the given test data and labels. """
        score = 0
        y = self.predict(X_test)
        for id in range(len(y_test)):
            if y[id] == y_test[id]:
                score += 1
        score /= len(X_test)
        return score

def clean(X):
    translator = str.maketrans("", "", string.punctuation)
    return X.translate(translator)
