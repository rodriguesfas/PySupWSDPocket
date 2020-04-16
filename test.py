#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pysupwsdpocket import PySupWSDPocket

sentence = 'The human brain is quite proficient at word-sense disambiguation.'
nlp = PySupWSDPocket(lang='en', model='semcor_omsti')
doc = nlp.wsd(raw_text=sentence)

print(doc)