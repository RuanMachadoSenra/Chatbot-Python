from goose3 import Goose
import random
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

g = Goose()
url = 'https://www.treinaweb.com.br/blog/como-um-desenvolvedor-junior-pode-virar-um-pleno'

noticia = g.extract(url)

texto = noticia.cleaned_text

# -- Boas Vindas -- #
boas_vindas_usuario = ('olá', 'opa', 'eae', 'oi')
boas_vindas_bot = ('olá', 'opa', 'bem-vindo', 'oi', 'como posso ajudá-lo?')

def mensagem_inicio(texto):
    for palavra in texto.split():
        if palavra.lower() in boas_vindas_usuario:
            return(random.choice(boas_vindas_bot))
