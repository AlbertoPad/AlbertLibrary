import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import spacy

nlp = spacy.load('es_core_news_sm')


def tokenizar(_texto):
    '''
    Tokeniza y devuelve frase_tokens=[tokens:lista, lang:str]
    '''
    
    tokens= word_tokenize(_texto) 
    tokens = [word.lower() for word in tokens if word.isalpha()]
    lang = detect(" ".join(tokens))
    frase_tokens=[tokens, lang]
    return frase_tokens

def clean_sw_english(_tokens):
    '''
    Función que limpia un lista de tokens. Parte de una variable 'frase_tokens' con forma [tokens, idioma]
    normalmente obtenida de la  funcion tokenizar(...)
    
    idiomas:
    'en': 'English',
    'zh': 'Chinese',
    'es': 'Spanish',
    'ar': 'Arabic',
    'fr': 'French',
    'pt': 'Portuguese',
    'de': 'German',
    'ja': 'Japanese',
    'ru': 'Russian',
    'ko': 'Korean',
    'it': 'Italian',
    'tr': 'Turkish',
    'id': 'Indonesian',
    'nl': 'Dutch',
    'pl': 'Polish',
    'sv': 'Swedish',
    'th': 'Thai',
    'no': 'Norwegian',
    'he': 'Hebrew',
    'hi': 'Hindi'
    '''
    clean_tokens=_tokens[0][:]
    if frase_tokens[1]=='en':
        for token in _tokens[0]:
            if token in stopwords.words('english'):
                clean_tokens.remove(token)
                
    elif frase_tokens[1]=='es':
        for token in _tokens[0]:
            if token in stopwords.words('spanish'):
                clean_tokens.remove(token)
            
    return clean_tokens

def stem_lem(_tokens):
    '''
    Función que stemmea o lematiza en funcion del idioma. Parte de una variable 'frase_tokens' con forma [tokens, idioma]
    
    '''
    stem_tokens=[]
    if frase_tokens[1]=='en':
        english_stemmer = SnowballStemmer('english')
        for token in _tokens:
            stem_tokens.append(english_stemmer.stem(token))        
        
    elif frase_tokens[1]=='es':
        nlp=spacy.load('es_core_news_sm')
        for token in nlp(' '.join(_tokens)):
            stem_tokens.append(token.lemma_)   
    
    return stem_tokens