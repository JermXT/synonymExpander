from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec

glove_file = datapath('./glove.840B.300d.txt')
tmp_file = get_tmpfile("glove.txt")
_ = glove2word2vec(glove_file, tmp_file)

model = KeyedVectors.load_word2vec_format(tmp_file)
word_vectors = model.wv
fname = get_tmpfile("glovevektors.kv")
word_vectors.save(fname)


print("done")

