#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess, json

from os import path

class PySupWSDPocket(object):

    def __init__(self, lang, model):
        self.lang = lang
        self.model = model

    def wsd(self, raw_text):
        HERE = path.abspath(path.dirname(__file__))
        JAR_FILE = HERE+'/supwsd-pocket.jar'

        args = [raw_text, self.lang, self.model]

        try:
            annotation = subprocess.check_output(['java', '-jar', JAR_FILE, *args], shell=False)
            return annotation
        except Exception as err:
            return err