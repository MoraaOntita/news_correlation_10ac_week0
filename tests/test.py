import unittest
from function import extract_countries, extract_domain

class TestFunctions(unittest.TestCase):

    def test_extract_countries(self):
        # Test cases for extract_countries function
        text1 = "The United States, China, and Russia are mentioned in this text."
        self.assertEqual(extract_countries(text1), ['united states', 'china', 'russia'])

        text2 = "The USA and Africa are important regions."
        self.assertEqual(extract_countries(text2), ['usa', 'africa'])

        text3 = "No countries mentioned in this text."
        self.assertEqual(extract_countries(text3), [])

    def test_extract_domain(self):
        # Test cases for extract_domain function
        url1 = "https://www.example.com/path/to/page"
        self.assertEqual(extract_domain(url1), "www.example.com")

        url2 = "ftp://ftp.example.com/path/to/file"
        self.assertEqual(extract_domain(url2), "ftp.example.com")

        url3 = "invalid_url"
        self.assertIsNone(extract_domain(url3))

if __name__ == '__main__':
    unittest.main()
