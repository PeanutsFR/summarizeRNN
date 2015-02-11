import os
import operator
from collections import Counter
import theano
from theano import tensor as TT
import numpy as np

data_dir = '../data/'

# displays a dictionnary
def display_dict(liste={}):
    for key,value in liste:
        print key, value

# creates freq_dict[words] = frequencies
def create_freq_dict(data_file='2013-01.txt'):
    freq_dict = Counter() # freq_dict["word"] = frequence
    file = open(os.path.join(data_dir,data_file))
    for line in file:
        words = line.split()
        # count words frequency of the title
        #if "TITLE:" in words:
        if "TITLE:" in words[:1]:
            for word in words[1:]:
                freq_dict[word] += 1
        # count words frequency of the body
        if "BODY:" in words[:1]:
            for word in words[1:]:
                freq_dict[word] += 1
    file.close()
    return freq_dict

# returns dictionnary (type=list) of top words by frequency
def top_freq_dict(freq_dict={}, topwords=10):
    top_freq_dict = dict(Counter(freq_dict).most_common(topwords-1))
    top_freq_dict["UNK"] = 5 # UNK word as the n-th top word
    return sorted(top_freq_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
    #return top_freq_dict

# create 1-of-n vectors corresponding to words ***
def word_to_vec(words=[]):
    vec_dict = {}
    len_words = len(words)
    i=0
    while i<len_words:
        vec = np.zeros(len_words)
        vec[i] = 1
        vec_dict[words[i]] = vec
        i += 1
    return vec_dict