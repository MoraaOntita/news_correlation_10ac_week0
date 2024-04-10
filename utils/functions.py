# Import necessary libraries if any
import spacy
from urllib.parse import urlparse

# Load spacy model
nlp = spacy.load("en_core_web_sm")

# List of countries, regions, and continents
countries_list = [
    'us', 'usa', 'united states', 'united states of america', 'america', 'united states of',
    'china', 'prc', 'people\'s republic of china',
    'russia', 'russian federation', 'soviet union', 'ussr',
    'ukraine', 'ukr', 'ukrainian',
    'middle east', 'middle eastern', 'mideast',
    'africa', 'african',
    'north america', 'north american', 'na',  # For USA
    'asia', 'asian', 'cn'  # For China
]

def extract_countries(text):
    doc = nlp(text)
    countries = [ent.text.lower() for ent in doc.ents if ent.label_ == "GPE" and ent.text.lower() in countries_list]
    return countries

def extract_domain(url):
    try:
        parsed_uri = urlparse(url)
        if parsed_uri.scheme == '' or parsed_uri.netloc == '':
            return None
        domain = '{uri.netloc}'.format(uri=parsed_uri)
        return domain
    except:
        return None