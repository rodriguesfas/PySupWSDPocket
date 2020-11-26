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

    def wsd(self, raw_text):
        HERE = path.abspath(path.dirname(__file__))
        JAR_FILE = HERE+'/supwsd-pocket.jar'

        args = [raw_text, self.lang, self.model, self.WORKSPACE]

        try:
            doc = subprocess.check_output(['java', '-jar', JAR_FILE, *args], shell=False)
            doc = doc.decode("utf-8")
            return doc
        except Exception as err:
            return err

