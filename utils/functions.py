
import spacy
from urllib.parse import urlparse

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

# Function to extract country mentions from text using spaCy
def extract_countries(text):
    doc = nlp(text)
    countries = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
    return countries

# Function to extract domain from URL
def extract_domain(url):
    try:
        parsed_uri = urlparse(url)
        domain = '{uri.netloc}'.format(uri=parsed_uri)
        return domain
    except:
        return None