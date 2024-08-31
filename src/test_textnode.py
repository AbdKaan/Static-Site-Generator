import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_eq_none(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

    def test_eq_property(self):
        node = TextNode("This is a text node", "strong", "boot.dev")
        node2 = TextNode("This is a text node", "strong", "boot.dev")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()