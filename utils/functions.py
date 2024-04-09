from urllib.parse import urlparse


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
    # Implementation of extract_countries function
    pass

def extract_domain(url):
    try:
        parsed_uri = urlparse(url)
        if parsed_uri.scheme == '' or parsed_uri.netloc == '':
            return None
        domain = '{uri.netloc}'.format(uri=parsed_uri)
        return domain
    except:
        return None

