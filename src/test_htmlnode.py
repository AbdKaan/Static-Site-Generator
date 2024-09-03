import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_starting_space(self):
        node = HTMLNode("p", "Test paragraph", None, {"class": "test-class"})
        html = node.props_to_html()
        assert html[0] == " "

    def test_props_to_html_type(self):
        node = HTMLNode("p", "Test paragraph", None, {"class": "test-class"})
        assert isinstance(node.props_to_html(), str)

    def test_props_to_html_multiple_props(self):
        node = HTMLNode("p", "Test paragraph", None, {"class": "test-class", "id":"sabaton"})
        assert node.props_to_html() == ' class="test-class" id="sabaton"'

    def test_default_parameters(self):
        node = HTMLNode()
        assert node.tag == None
        assert node.value == None
        assert node.children == None
        assert node.props == {}

if __name__ == "__main__":
    unittest.main()