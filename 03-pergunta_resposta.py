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

#vetor_palavras = TfidfVectorizer()
#palavras_rotuladas = vetor_palavras.fit_transform(texto_principal)
#print(palavras_rotuladas)
#print(vetor_palavras.get_feature_names()) # palavras únicas
#print(vetor_palavras.vocabulary_) # id das palavras

#similaridade = cosine_similarity(palavras_rotuladas[0], palavras_rotuladas[2])
#similaridade_todos = cosine_similarity(palavras_rotuladas[0], palavras_rotuladas)
#print(similaridade_todos)
#print(similaridade_todos.argsort())
#x = similaridade_todos.argsort()[0]
#print(x[-2])

def resposta(texto_usuario):
    resposta_bot = ''
    texto_principal.append(texto_usuario)
    tfidf = TfidfVectorizer()
    palavras_rotuladas = tfidf.fit_transform(texto_principal)
    similaridade = cosine_similarity(palavras_rotuladas[-1], palavras_rotuladas)
    indice_similaridade = similaridade.argsort()[0][-2]
    vetor_similaridade = similaridade.flatten()
    vetor_similaridade.sort()
    vetor_encontrado = vetor_similaridade[-2]

    if(vetor_encontrado == 0):
        resposta_bot = resposta_bot + 'Desculpe, mas não entendi'
        return resposta_bot
    else:
        resposta_bot = resposta_bot + texto_principal[indice_similaridade]
        return resposta_bot
