from goose3 import Goose
import random
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

g = Goose()
url = 'https://www.treinaweb.com.br/blog/como-um-desenvolvedor-junior-pode-virar-um-pleno'

noticia = g.extract(url)

texto = noticia.cleaned_text

print(texto)

