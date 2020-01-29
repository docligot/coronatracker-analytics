import json
import gensim
import nltk
import numpy as np
import pandas as pd
import pickle
import pyLDAvis.gensim
import random
import spacy
import yaml
from gensim import corpora
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
spacy.load('en_core_web_sm')
from spacy.lang.en import English
nltk.download('wordnet')
nltk.download('stopwords')

def config_args(config):
    """Return arguments from the configuration file.
    Keyword arguments:
    config -- the configuration file that contains the parameters needed for the program.
    """
    with open('config.yaml', 'rb') as file:
        conf = yaml.safe_load(file)
    return conf['lda']

def tokenize(text):
    """Return tokenized texts from the input text.
    Keyword arguments:
    text -- the line(s) of text to be tokenized.
    """
    lda_tokens = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            pass
        elif token.orth_.startswith('@'):
            pass
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens

def get_lemma(word):
    """Return lemmatized word from the input text.
    Keyword arguments:
    word -- the line(s) of text to be lemmatized.
    """
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma

def get_lemma2(word):
    """Return lemmatized word from the input text.
    Keyword arguments:
    word -- the line(s) of text to be lemmatized.
    """
    return WordNetLemmatizer().lemmatize(word)



def prepare_text_for_lda(text):
    """Return processed texts for model fitting.
    Keyword arguments:
    text -- the line(s) of text to be preprocessed.
    """
    tokens = tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma(token) for token in tokens]
    return tokens

#Get args from config file
args = config_args('config.yaml')
num_topics = args['num_topics']
num_passes = args['num_passes']
num_words_topics = args['num_words_topics']
sort_topics = args['sort_topics']

#Load dataset
data_list = []
with open('datasets/data.json') as file:
    data = json.load(file)
    for text in data:
        data_list.append(text['text'])
data_series = pd.Series(data_list)

parser = English()
en_stop = set(nltk.corpus.stopwords.words('english'))

#Pre-process the dataset
text_data = []
for line in data_series:
    tokens = prepare_text_for_lda(line)
    if random.random() > .99:
        print(tokens)
        text_data.append(tokens)

#Create dictionary from the dataset
dictionary = corpora.Dictionary(text_data)
corpus = [dictionary.doc2bow(text) for text in text_data]
pickle.dump(corpus, open('artifacts/corpus.pkl', 'wb'))
dictionary.save('artifacts/dictionary.gensim')

#Create and save LDA mode
lda_model = gensim.models.ldamodel.LdaModel(corpus, num_topics = num_topics, id2word=dictionary, passes=num_passes)
lda_model.save('artifacts/model.gensim')
topics = lda_model.print_topics(num_words=num_words_topics)

#Visualize LDA Topic Modeling
dictionary = gensim.corpora.Dictionary.load('artifacts/dictionary.gensim')
corpus = pickle.load(open('artifacts/corpus.pkl', 'rb'))
lda = gensim.models.ldamodel.LdaModel.load('artifacts/model.gensim')
lda_display = pyLDAvis.gensim.prepare(lda, corpus, dictionary, sort_topics=sort_topics)
pyLDAvis.save_html(lda_display,'ncov-topic-model.html')