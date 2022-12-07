from nltk.chat.util import Chat, reflections

expressoes_pt = {
    'eu': 'você',
    'eu sou': 'você é',
    'eu era': 'você era',
    'eu iria': 'você iria',
    'eu irei': 'você irá',
    'meu': 'seu',
    'você': 'eu',
    'você é': 'eu sou',
    'você era': 'eu era',
    'você irá': 'eu irei',
    'seu': 'meu',
}

sentencas = [
    [
       r'oi|olá|opa|eae',
        ['olá', 'como vai?', 'tudo bem?']
    ],
    [
        r'qual é o seu nome?',
        ['Meu nome é TwBot.  Em que posso ajudá-lo?']
    ],
    [
        r'(.*) sua idade',
        ['Não tenho idade pois sou um chatbot']
    ],
    [
        r'meu nome é (.*)',
        ['Olá %1, como você está hoje?']
    ],
    [
        r'qual formação você indica em Python?',
        ['Formação Flask', 'Formação Django', 'Formação ML com Python']
    ],
    [
        r'quais tecnologias estão em alta no mercado?',
        ['Flutter', 'React', 'NextJS']
    ],
    [
        r'quit',
        ['Até breve', 'Foi bom conversar com você.']
    ]
]

print("Olá, sou o TwBot")
chat = Chat(sentencas, expressoes_pt)
chat.converse()