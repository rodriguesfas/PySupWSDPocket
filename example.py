from pysupwsdpocket import PySupWSDPocket

import json

sentence = 'The human brain is quite proficient at word-sense disambiguation.'

nlp = PySupWSDPocket(lang='en', model='semcor_omsti', model_path="/home/USER/pysupwsdpocket_models")
doc = nlp.wsd(raw_text=sentence)

print(doc)