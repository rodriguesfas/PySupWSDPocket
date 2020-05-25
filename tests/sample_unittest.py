#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from pysupwsdpocket import PySupWSDPocket

class TestBoostPathosUnittest(unittest.TestCase):

    def __init__(self):
        self.expected_out = '[ { "token": { "word": "The", "tag": "DT", "pos": "NOUN", "lemma": "the" }, "senses": [ { "id": "U", "probability": 1.0 } ] }, { "token": { "word": "human", "tag": "JJ", "pos": "ADJ", "lemma": "human" }, "senses": [ { "id": "human%3:01:00::", "probability": 0.5186562830274255 }, { "id": "human%3:00:00::", "probability": 0.24960670716780253 }, { "id": "human%3:01:01::", "probability": 0.2317370098047719 } ] }, { "token": { "word": "brain", "tag": "NN", "pos": "NOUN", "lemma": "brain" }, "senses": [ { "id": "brain%1:08:00::", "probability": 0.41164696630447617 }, { "id": "brain%1:18:00::", "probability": 0.21535601314321137 }, { "id": "brain%1:09:00::", "probability": 0.18750595505954415 }, { "id": "brain%1:09:01::", "probability": 0.18549106549276823 } ] }, { "token": { "word": "is", "tag": "VBZ", "pos": "VERB", "lemma": "be" }, "senses": [ { "id": "be%2:42:03::", "probability": 0.22342081210545192 }, { "id": "be%2:42:06::", "probability": 0.08343524647397425 }, { "id": "be%2:42:09::", "probability": 0.0780860178423599 }, { "id": "be%2:42:05::", "probability": 0.07767209551986816 }, { "id": "be%2:42:01::", "probability": 0.07405223148248687 }, { "id": "be%2:42:02::", "probability": 0.07318010761333324 }, { "id": "be%2:40:00::", "probability": 0.07225047965136297 }, { "id": "be%2:42:08::", "probability": 0.06909834491603184 }, { "id": "be%2:42:00::", "probability": 0.06742651514056155 }, { "id": "be%2:41:00::", "probability": 0.06528517138653986 }, { "id": "be%2:42:04::", "probability": 0.05894378337741274 }, { "id": "be%2:42:07::", "probability": 0.057149194490616624 } ] }, { "token": { "word": "quite", "tag": "RB", "pos": "ADV", "lemma": "quite" }, "senses": [ { "id": "quite%4:02:02::", "probability": 0.4294685929011319 }, { "id": "quite%4:02:01::", "probability": 0.35128873648957576 }, { "id": "quite%4:02:03::", "probability": 0.2192426706092924 } ] }, { "token": { "word": "proficient", "tag": "JJ", "pos": "ADJ", "lemma": "proficient" }, "senses": [ { "id": "proficient%5:00:00:skilled:00", "probability": 1.0 } ] }, { "token": { "word": "at", "tag": "IN", "pos": "ADV", "lemma": "at" }, "senses": [ { "id": "U", "probability": 1.0 } ] }, { "token": { "word": "word-sense", "tag": "NN", "pos": "NOUN", "lemma": "word-sense" }, "senses": [ { "id": "U", "probability": 1.0 } ] }, { "token": { "word": "disambiguation", "tag": "NN", "pos": "NOUN", "lemma": "disambiguation" }, "senses": [ { "id": "U", "probability": 1.0 } ] }, { "token": { "word": ".", "tag": ".", "pos": "NOUN", "lemma": "." }, "senses": [ { "id": "U", "probability": 1.0 } ] } ]'
        self.sentence = 'The human brain is quite proficient at word-sense disambiguation.'

    def main(self):
        nlp = PySupWSDPocket(lang='en', model='semcor_omsti')
        doc = nlp.wsd(raw_text=self.sentence)
        self.assertEqual(doc, self.expected_out, "Err output!")

if __name__ == "__main__":
    unittest.main()