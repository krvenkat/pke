#!/usr/bin/env python
# -*- coding: utf-8 -*-

# this example uses TopicRank
from pke.unsupervised import TopicRank

# create a TopicRank extractor and set the input language to English (used for
# the stoplist in the candidate selection method)
extractor = TopicRank(input_file='C-1.xml',
                      language='english')

# load the content of the document, here in CoreNLP XML format
# the use_lemmas parameter allows to choose using CoreNLP lemmas or stems 
# computed using nltk
extractor.read_document(format='corenlp',
                        use_lemmas=False)

# select the keyphrase candidates, for TopicRank the longest sequences of 
# nouns and adjectives
extractor.candidate_selection(pos=['NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'JJR',
                                   'JJS'])

# weight the candidates using a random walk. The threshold parameter sets the
# minimum similarity for clustering, and the method parameter defines the 
# linkage method
extractor.candidate_weighting(threshold=0.74,
                              method='average')

# print the n-highest (10) scored candidates
for (keyphrase, score) in extractor.get_n_best(n=10):
	print(keyphrase, score)