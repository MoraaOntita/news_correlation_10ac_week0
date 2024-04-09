import unittest
from unittest.mock import Mock
import pandas as pd
import spacy
from urllib.parse import urlparse  # Importing urlparse from urllib.parse

# Function to extract country mentions from text using spaCy
def extract_countries(text, nlp=None):
    if nlp is None:
        nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    countries = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
    return countries

# Function to extract domain from URL
def extract_domain(url):
    try:
        parsed_uri = urlparse(url)
        if parsed_uri.netloc:
            domain = '{uri.netloc}'.format(uri=parsed_uri)
            return domain
        else:
            return None
    except:
        return None

class TestExtractCountries(unittest.TestCase):
    def setUp(self):
        # Mock spaCy's nlp object
        self.mock_nlp = Mock()
        self.mock_nlp.return_value = Mock(ents=[])

    def test_single_entity(self):
        # Test with a single entity
        self.mock_nlp.return_value.ents = [Mock(text="United States", label_="GPE")]
        text = "The United States is a country."
        countries = extract_countries(text, nlp=self.mock_nlp)
        self.assertEqual(countries, ["United States"])

    def test_multiple_entities(self):
        # Test with multiple entities
        self.mock_nlp.return_value.ents = [
            Mock(text="United States", label_="GPE"),
            Mock(text="Canada", label_="GPE"),
            Mock(text="Mexico", label_="GPE")
        ]
        text = "The United States, Canada, and Mexico are countries."
        countries = extract_countries(text, nlp=self.mock_nlp)
        self.assertEqual(countries, ["United States", "Canada", "Mexico"])

    def test_no_entity(self):
        # Test with no entities
        text = "There are no countries mentioned."
        countries = extract_countries(text, nlp=self.mock_nlp)
        self.assertEqual(countries, [])

    def test_mixed_entities(self):
        # Test with mixed entities
        self.mock_nlp.return_value.ents = [
            Mock(text="United States", label_="GPE"),
            Mock(text="person", label_="PERSON")
        ]
        text = "The United States is a country. John is a person."
        countries = extract_countries(text, nlp=self.mock_nlp)
        self.assertEqual(countries, ["United States"])

class TestExtractDomain(unittest.TestCase):
    def test_valid_url(self):
        # Test with a valid URL
        url = "https://www.example.com/page"
        domain = extract_domain(url)
        self.assertEqual(domain, "www.example.com")

    def test_invalid_url(self):
        # Test with an invalid URL
        url = "not a valid url"
        domain = extract_domain(url)
        self.assertIsNone(domain)

    def test_no_scheme(self):
        # Test with a URL without a scheme (e.g., http:// or https://)
        url = "www.example.com/page"
        domain = extract_domain(url)
        self.assertEqual(domain, "www.example.com")

if __name__ == '__main__':
    unittest.main()
