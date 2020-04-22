#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse, re

from os import path
from codecs import open

from pysupwsdpocket import PySupWSDPocket

HERE = path.abspath(path.dirname(__file__))

def wsd(raw_text, lang, model):
    if raw_text and lang and model:
        nlp = PySupWSDPocket(lang=lang, model=model)
        doc = nlp.wsd(raw_text=raw_text)
        return doc
    else:
        print("Wrong command!")
        print("Try the command: pysupwsdpocket --wsd [sentence|corpus] [lang] [model]")

def install(model):
    if model:
        PySupWSDPocket().install(model)
    else:
        print("Wrong command!")
        print("Try the command: pysupwsdpocket --install [model]")

def main():
    my_parser = argparse.ArgumentParser(
        prog="pysupwsdpocket",
        description="Just a Python Version of SupWSD Pocket: A software suite for SUPervised Word Sense Disambiguation."
    )

    version_file_contents = open(path.join(HERE, '_version.py'), encoding='utf-8').read()
    VERSION = re.compile('__version__ = \"(.*)\"').search(version_file_contents).group(1)
    my_parser.version = 'PySupWSDPocket V-' + VERSION

    my_parser.add_argument('-v', '--version',
                           help='Show version.',
                           action='version')

    my_parser.add_argument('-wsd', '--wsd',
                        help="Run WSD",
                        type=wsd,
                        action='store')

    my_parser.add_argument('-install', '--install',
                        help="Install Model Language.",
                        type=install,
                        action='store')

    try:
        raw_text, lang, model = my_parser.parse_args()
    except Exception as error:
        pass
    else:
        model = my_parser.parse_args()
    finally:
        pass

if __name__ == '__main__':
    main()
