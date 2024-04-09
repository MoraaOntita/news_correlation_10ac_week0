import unittest
from unittest.mock import Mock
import pandas as pd
import spacy

# Function to extract country mentions from text using spaCy
def extract_countries(text, nlp=None):
    if nlp is None:
        nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    countries = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
    return countries

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

if __name__ == '__main__':
    unittest.main()
