from pysupwsdpocket import PySupWSDPocket

import json

sentence = 'The human brain is quite proficient at word-sense disambiguation'

nlp = PySupWSDPocket(lang='en', model='semcor_omsti', model_path="/home/USER/pysupwsdpocket_models")
doc = nlp.wsd(raw_text=sentence)

for token in doc.tokens():
    print(token.word, token.lemma, token.pos, token.max_probability())

disambiguated = nlp.disambiguate(sentence, "human")
print(disambiguated)

print("\nPARSING A ENTIRE CORPUS\n")

docs = nlp.parse_corpus("./example_corpus.txt")
for doc in docs:
    print(doc._text)
    for token in doc.tokens():
        print(token.word, token.lemma, token.pos, token.max_probability())
    print()