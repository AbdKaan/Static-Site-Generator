import unittest

from main_helper_functions import extract_title


class TestHTMLNode(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Palantir\nThat is a palantir."
        assert "Palantir" == extract_title(markdown)

if __name__ == "__main__":
    unittest.main()