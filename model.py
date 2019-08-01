from spacy.lang.en.stop_words import STOP_WORDS
from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from gensim.test.utils import datapath

fname = get_tmpfile("glovevektors.kv")
word_vectors = KeyedVectors.load(fname, mmap='r')

