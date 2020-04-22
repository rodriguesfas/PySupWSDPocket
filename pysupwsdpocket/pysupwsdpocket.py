#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess, json, os, sys

from os import path

class PySupWSDPocket(object):

    def __init__(self, lang, model):
        self.lang = lang
        self.model = model

        self.HOME = os.environ['HOME']
        self.PATH_MODELS = '/pysupwsdpocket_models'

    def wsd(self, raw_text):
        HERE = path.abspath(path.dirname(__file__))
        JAR_FILE = HERE+'/supwsd-pocket.jar'
        workspace = self.HOME + '/pysupwsdpocket_models'

        args = [raw_text, self.lang, self.model, workspace]

        try:
            annotation = subprocess.check_output(['java', '-jar', JAR_FILE, *args], shell=False)
            return annotation
        except Exception as err:
            return err

    def install(self, model, link_model):
        from homura import download

        # check folder plugin exist.
        if not os.path.exists(self.HOME+self.PATH_MODELS):
            os.makedirs(self.HOME+self.PATH_MODELS)

        # Download plugin.
        print("Downloading model", model, "..")
        download(url=link_model, path=self.HOME+self.PATH_MODELS)

        print("Plugin", model, "installed!")
        print("Path of installed model:", self.HOME+self.PATH_MODELS)
        sys.exit(0)

    def uninstall(self, model):
        try:
            print("Uninstall plugin", model, "..")
            os.remove(self.HOME+self.PATH_MODELS)
            print("Model", model, "unistalled!")
        except Exception as err:
            print("Model not found!")