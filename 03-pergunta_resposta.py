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
            
texto = sent_tokenize(texto)

texto_principal = texto[:3]
texto_principal.append(texto_principal[0])

vetor_palavras = TfidfVectorizer()
palavras_rotuladas = vetor_palavras.fit_transform(texto_principal)
#print(palavras_rotuladas)
#print(vetor_palavras.get_feature_names()) # palavras únicas
#print(vetor_palavras.vocabulary_) # id das palavras

similaridade = cosine_similarity(palavras_rotuladas[0], palavras_rotuladas[2])
similaridade_todos = cosine_similarity(palavras_rotuladas[0], palavras_rotuladas)
print(similaridade_todos)
print(similaridade_todos.argsort())
x = similaridade_todos.argsort()[0]
print(x[-2])
