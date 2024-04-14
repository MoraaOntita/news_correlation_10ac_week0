import unittest
import pandas as pd
from utils.functions import extract_countries, extract_domain, preprocess_text, extract_keywords

class TestFunctions(unittest.TestCase):
    def test_extract_countries(self):
        # Test case with a sample text
        text = "I visited China and Russia yesterday."
        expected_countries = ['china', 'russia']
        self.assertEqual(extract_countries(text), expected_countries)

        # Test case with no countries mentioned
        text = "The weather was nice today."
        self.assertEqual(extract_countries(text), [])

    def test_extract_domain(self):
        # Test case with a valid URL
        url = "https://www.example.com/somepage"
        expected_domain = "www.example.com"
        self.assertEqual(extract_domain(url), expected_domain)

        # Another valid URL
        url2 = "http://subdomain.example.com/path/to/page"
        expected_domain2 = "subdomain.example.com"
        self.assertEqual(extract_domain(url2), expected_domain2)

        # Yet another valid URL
        url3 = "https://www.example.co.uk"
        expected_domain3 = "www.example.co.uk"
        self.assertEqual(extract_domain(url3), expected_domain3)
        
    def test_preprocess_text(self):
        # Test case with sample text
        text = "I visited China and Russia yesterday. The weather was nice today."
        expected_output = "visited china russia yesterday weather nice today"
        self.assertEqual(preprocess_text(text), expected_output)

    # Add more test cases for preprocess_text if needed

    def test_extract_keywords(self):
        # Create a sample DataFrame for testing
        df_data = pd.DataFrame({'content': ["I visited China and Russia yesterday.",
                                            "The weather was nice today."]})
        # Call extract_keywords function
        top_keywords = extract_keywords(df_data)
        
        # Assert the output
        self.assertGreaterEqual(len(top_keywords), 7)  # Ensure at least 7 keywords are extracted
        # Add more assertions if needed

if __name__ == '__main__':
    unittest.main()


