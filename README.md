# Synonym Expander

to setup:
download http://nlp.stanford.edu/data/wordvecs/glove.840B.300d.zip and place in this directory
python3 converter.py

run microservice:
python3 service.py

Dependencies:
pip3 install spacy
python3 -m spacy download en\_core\_web\_sm
pip3 install gensim


Note:
needs ~4.5 GB of free RAM to run
