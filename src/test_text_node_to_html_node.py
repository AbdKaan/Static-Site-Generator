import unittest

from helper_functions import text_node_to_html_node
from leafnode import LeafNode
from textnode import TextNode


class TestConverter(unittest.TestCase):
    def test_type(self):
        node = TextNode("Fus Ro Dah", "text")
        html_node = text_node_to_html_node(node)
        assert isinstance(html_node, LeafNode)

    def test_text(self):
        node = TextNode("Fus Ro Dah", "text")
        html_node = text_node_to_html_node(node)
        assert html_node.tag == None
        assert html_node.value == "Fus Ro Dah"

    def test_bold(self):
        node = TextNode("Bold of you to assume that", "bold")
        html_node = text_node_to_html_node(node)
        assert html_node.tag == 'b'
        assert html_node.value == "Bold of you to assume that"

    def test_italic(self):
        node = TextNode("Italia", "italic")
        html_node = text_node_to_html_node(node)
        assert html_node.tag == 'i'
        assert html_node.value == "Italia"

    def test_code(self):
        node = TextNode("print('Hello World')", "code")
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "code"
        assert html_node.value == "print('Hello World')"

    def test_link(self):
        node = TextNode("boot.dev", "link", "boot.dev")
        html_node = text_node_to_html_node(node)
        assert html_node.tag == 'a'
        assert html_node.value == "boot.dev"
        assert html_node.props['href'] == "boot.dev"

    def test_image(self):
        node = TextNode("duck", "image", "https://cdn.britannica.com/92/100692-050-5B69B59B/Mallard.jpg")
        html_node = text_node_to_html_node(node)
        assert html_node.tag == 'img'
        assert html_node.props['src'] == "https://cdn.britannica.com/92/100692-050-5B69B59B/Mallard.jpg"
        assert html_node.props['alt'] == "duck"

if __name__ == "__main__":
    unittest.main()