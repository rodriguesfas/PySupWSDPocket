#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess, json, os

from os import path

class PySupWSDPocket(object):

    def __init__(self, lang, model, model_path = None):
        self.lang = lang
        self.model = model

        if model_path is None:
            self.WORKSPACE = os.environ['HOME'] + '/pysupwsdpocket_models'
        else:
            self.WORKSPACE = model_path

    def parse_corpus(self, corpus_path):
        HERE = path.abspath(path.dirname(__file__))
        JAR_FILE = HERE+'/supwsd-pocket.jar'

        args = [corpus_path, self.lang, self.model, self.WORKSPACE]

        try:
            json_raw = subprocess.check_output(['java', '-jar', JAR_FILE, *args], shell=False).decode("utf-8")
            json_docs = json_raw.split("\n\n")
            docs = []
            for json_doc in json_docs:
                yield Document(json_doc)
        except Exception as err:
            return err

    def wsd(self, raw_text):
        HERE = path.abspath(path.dirname(__file__))
        JAR_FILE = HERE+'/supwsd-pocket.jar'

        args = [raw_text, self.lang, self.model, self.WORKSPACE]

        try:
            json_raw = subprocess.check_output(['java', '-jar', JAR_FILE, *args], shell=False).decode("utf-8")
            doc = Document(json_raw)
            return doc
        except Exception as err:
            return err
    
    def disambiguate(self, raw_text, ambiguous, word_lemmatized=False):
        doc = self.wsd(raw_text)
        for token in doc.tokens():
            if word_lemmatized and ambiguous == token.lemma:
                return token.max_probability()
            if not word_lemmatized and ambiguous == token.word:
                return token.max_probability()

class Document():
    def __init__(self, json_raw):
        json_raw_lines = json_raw.splitlines()
        self._tokens = []
        self._text = json_raw_lines[0]
        self._json_raw = "\n".join(json_raw_lines[1:])
        self._json_object = {
            "tokens": json.loads(self._json_raw),
            "raw_text": self._text
        }
        for token_ in self._json_object['tokens']:
            self._tokens.append(Token(token_))
    
    def __repr__(self):
        return json.dumps(self._json_object)

    def json_parse(self):
        for token in self._json_object['tokens']:
            self._tokens.append(Token(token))
    
    def tokens(self):
        return self._tokens
    
    

class Token():
    def __init__(self, json_dict):
        self.word = json_dict['token']['word']
        self.pos = json_dict['token']['tag']
        self.lemma = json_dict['token']['lemma']
        if "senses" in json_dict:
            self.senses = json_dict['senses']
        else:
            self.senses =[]
    
    def __repr__(self):
        if self.senses is not None:
            return "{0} => {1}".format(self.word, self.max_probability()['id'])
        else:
            return self.word
    
    def __str__(self):
        return self.__repr__()
    
    def max_probability(self):
        if len(self.senses) > 0:
            results=sorted(self.senses,key=lambda k:k['probability'],reverse=True)
            return results[0]
    

