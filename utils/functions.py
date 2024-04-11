# Import necessary libraries if any
import spacy
from urllib.parse import urlparse
import re
import string
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')

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
    
def preprocess_text(text):
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove emojis
    text = text.encode('ascii', 'ignore').decode('ascii')
    # Remove emoticons
    text = re.sub(r':\)|;\)|:-\)|:-\(|:-D|:-\(|:-\)|:D|:P|:S|:\||:O|:\(|:\-D|:\-S', '', text)
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize text
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    # Lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    # Join tokens back into a single string
    preprocessed_text = ' '.join(tokens)
    return preprocessed_text

def extract_keywords(df_data):
    # Apply text preprocessing to 'content' column
    df_data['clean_content'] = df_data['content'].apply(preprocess_text)
    
    # Perform TF-IDF vectorization with even higher max_features
    tfidf_vectorizer = TfidfVectorizer(max_features=20000)
    tfidf_matrix = tfidf_vectorizer.fit_transform(df_data['clean_content'])

    # Get feature names (words)
    feature_names = tfidf_vectorizer.get_feature_names_out()
    
    print("Feature Names:")
    print(feature_names)

    # Create a DataFrame from TF-IDF matrix
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)

    # Identify top keywords
    top_keywords = tfidf_df.sum().sort_values(ascending=False).head(10)
    
    # Return top_keywords as a list
    return top_keywords.index.tolist()  # Return list of top keywords
