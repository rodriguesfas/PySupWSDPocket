#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, sys, argparse

from os import path
from codecs import open
from pysupwsdpocket import PySupWSDPocket

HERE = path.abspath(path.dirname(__file__))

def wsd(raw_text, lang, model):
    if raw_text and lang and model:
        nlp = PySupWSDPocket(lang=lang, model=model)
        doc = nlp.wsd(raw_text=raw_text)
        print(doc)
    else:
        print("Wrong command!")
        print("Try the command: pysupwsdpocket --wsd [sentence|corpus] [lang] [model]")

def main():
    parser = argparse.ArgumentParser(
        prog="pysupwsdpocket",
        description="Just a Python Version of SupWSD Pocket: A software suite for SUPervised Word Sense Disambiguation."
    )

    version_file_contents = open(path.join(HERE, '_version.py'), encoding='utf-8').read()
    VERSION = re.compile('__version__ = \"(.*)\"').search(version_file_contents).group(1)
    parser.version = 'PySupWSDPocket V-' + VERSION

    parser.add_argument('-v', '--version',
                           help='Show version.',
                           action='version')

    parser.add_argument('-wsd', '--wsd',
                        nargs=5,
                        help="Run WSD")

    if(sys.argv[1] in ['-wsd', '--wsd']):
        raw_text, lang, model = sys.argv[2], sys.argv[3], sys.argv[4]
        wsd(raw_text, lang, model)


if __name__ == '__main__':
    main()
