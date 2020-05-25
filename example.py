from pysupwsdpocket import PySupWSDPocket

import json

sentence = 'The human brain is quite proficient at word-sense disambiguation.'

nlp = PySupWSDPocket(lang='en', model='semcor_omsti')
doc = nlp.wsd(raw_text=sentence)

for token in doc.tokens():
    print(token.word, token.lemma, token.pos, token.max_probability())

disambiguated = nlp.disambiguate(sentence, "human")
print(disambiguated)