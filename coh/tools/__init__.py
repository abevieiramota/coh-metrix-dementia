# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division

from coh.tools.tag import *

pos_tagger = OpenNLPTagger()

from coh.tools.tokenizers import senter, word_tokenize
from coh.tools.syllable import *
from coh.tools.stemmers import DelafStemmer

stemmer = DelafStemmer()