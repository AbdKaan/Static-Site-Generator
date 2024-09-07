import unittest

from textnode import TextNode
from helper_functions import split_nodes_delimiter


class TestLeafNode(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextNode.text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", TextNode.text_type_code)
        result = [
                    TextNode("This is text with a ", TextNode.text_type_text),
                    TextNode("code block", TextNode.text_type_code),
                    TextNode(" word", TextNode.text_type_text),
                ]

        assert new_nodes == result

    def test_italic(self):
        node = TextNode("This is text with an *italic* word", TextNode.text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", TextNode.text_type_italic)
        result = [
                    TextNode("This is text with an ", TextNode.text_type_text),
                    TextNode("italic", TextNode.text_type_italic),
                    TextNode(" word", TextNode.text_type_text),
                ]

        assert new_nodes == result

    def test_text_type_not_text(self):
        node = TextNode("This is some code", TextNode.text_type_code)
        new_nodes = split_nodes_delimiter([node])
        result = [TextNode("This is some code", TextNode.text_type_code)]

        assert new_nodes == result

    def test_multiple_segments(self):
        node = TextNode("This is text with a `code block` word and `another code block`", TextNode.text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", TextNode.text_type_code)
        result = [
                    TextNode("This is text with a ", TextNode.text_type_text),
                    TextNode("code block", TextNode.text_type_code),
                    TextNode(" word and ", TextNode.text_type_text),
                    TextNode("another code block", TextNode.text_type_code),
                ]

        assert new_nodes == result
    
    def test_multiple_old_nodes(self):
        node = TextNode("This is text with a `code block` word and `another code block`", TextNode.text_type_text)
        node2 = TextNode("This is text with a `code block` word", TextNode.text_type_text)
        new_nodes = split_nodes_delimiter([node, node2], "`", TextNode.text_type_code)
        result = [
                    TextNode("This is text with a ", TextNode.text_type_text),
                    TextNode("code block", TextNode.text_type_code),
                    TextNode(" word and ", TextNode.text_type_text),
                    TextNode("another code block", TextNode.text_type_code),
                    TextNode("This is text with a ", TextNode.text_type_text),
                    TextNode("code block", TextNode.text_type_code),
                    TextNode(" word", TextNode.text_type_text)
                ]

        assert new_nodes == result


if __name__ == "__main__":
    unittest.main()