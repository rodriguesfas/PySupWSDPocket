# PySupWSDPocket
Just a Python Version of SupWSD Pocket: A software suite for SUPervised Word Sense Disambiguation.

# Suport langugae
- en, fr, de, it, es.

# Suport Model
- the model to be used in the disambiguation process: SEMCOR (English only), SEMCOR_OMSTI (English only), TRAIN_O_MATIC.<br/>
If you don't specify the model, the program will load the default one: ```semcor_omsti``` for English, ```train_o_matic``` for other languages.

# Installing

    pip install pysupwsdpocket

    or

    pip install pysupwsdpocket -U

# Install Model Language
[Download](https://supwsd.net/supwsd/downloads.jsp) the templates to the path: ```/home/your_user/pysupwsdpocket_models```

# Links Models
- EN: https://helsinkifi-my.sharepoint.com/:u:/g/personal/raganato_ad_helsinki_fi/EcISNoRjksJHgSY3hqcdsfAB-dQ3aVlC9Zs-Ppu3S24rSw?e=HzWRaD

- FR: https://helsinkifi-my.sharepoint.com/:u:/g/personal/raganato_ad_helsinki_fi/ERRz3CFpQVZOneka0NiXbQMB6J24LgxDgk04xQs9iX8t7w?e=JLRnwO

- DE: https://helsinkifi-my.sharepoint.com/:u:/g/personal/raganato_ad_helsinki_fi/ER1Gag9eBWVCsc5kDSYozgMBklegV74loBGZkqaQih9agQ?e=6Pvr2s

- IT: https://helsinkifi-my.sharepoint.com/:u:/g/personal/raganato_ad_helsinki_fi/EXUBDfiS5bxLqMBdDs4p3VwBE5PFdCaHJRdpE-8rGkGbRQ?e=YK9sEc

- ES: https://helsinkifi-my.sharepoint.com/:u:/g/personal/raganato_ad_helsinki_fi/EZRL8t0uqXBJqh60dPQXFskBJAAYUkDTBMl_P3RrL9NLXA?e=BY05hK

# Guide Start
```example.py```

```python
from pysupwsdpocket import PySupWSDPocket

sentence = 'The human brain is quite proficient at word-sense disambiguation.'

nlp = PySupWSDPocket(lang='en', model='semcor_omsti')
doc = nlp.wsd(raw_text=sentence)
print(doc)
```

# Running CLI
```sentence```	the sentence to be analyzed. <br>
```dataset```	the path of the file containing the sentences to be analyzed (one sentence per line).

```pysupwsd -wsd <sentence|dataset> <lang> <model>```

```shell
pysupwsdpocket -wsd 'The human brain is quite proficient at word-sense disambiguation.' en semcor_omsti
```

# Credits
- [SupWSD Site Oficial](https://supwsd.net/supwsd/index.jsp)<br>
- [SupWSD Github Oficial](https://github.com/SI3P/supWSD)<br>
- [Simone Papandrea](https://www.linkedin.com/in/simone-papandrea/)
- [Alessandro Raganato](https://github.com/raganato)