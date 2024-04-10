import unittest
from utils.functions import extract_countries, extract_domain

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

if __name__ == '__main__':
    unittest.main()


