#import numpy as np
import os
import operator
from collections import Counter

data_dir = '../data/'

# calculate words frequency in all articles [body + title]
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
        if "BODY:" in words:
            for word in words[1:]:
                freq_dict[word] += 1

    return freq_dict

# displays the n-best words sorted by frequency
def display_freq_dict(freq_dict={}, topwords=10):
    for word,frequence in freq_dict.most_common(topwords):
        print word, frequence