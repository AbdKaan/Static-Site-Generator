import unittest

from helper_functions import markdown_to_html_node
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        html_node = markdown_to_html_node(markdown)
        result = HTMLNode(children=[ParentNode(tag="h1", children=[LeafNode(value="This is a heading")]),
                                    ParentNode(tag="p", children=[LeafNode(value="This is a paragraph of text. It has some "),
                                                                    LeafNode("b", "bold"),
                                                                    LeafNode(value=" and "),
                                                                    LeafNode("i", "italic"),
                                                                    LeafNode(value=" words inside of it.")]),
                                    ParentNode(tag="ul", children=[ParentNode("li", children=[LeafNode(value="This is the first list item in a list block")]),
                                                                     ParentNode("li", children=[LeafNode(value="This is a list item")]),
                                                                     ParentNode("li", children=[LeafNode(value="This is another list item")])])]
                                      )

        assert html_node.__repr__() == result.__repr__()
        assert html_node.children[0].to_html() == result.children[0].to_html()
        assert html_node.children[1].to_html() == result.children[1].to_html()
        assert html_node.children[2].to_html() == result.children[2].to_html()

    def test2(self):
        markdown = "### This is a heading\n\n```This is a paragraph of text. It has some **bold** and *italic* words inside of it.```\n\n1. This is the first *list* item in a list block\n2. This is a list item\n3. This is another list item"
        html_node = markdown_to_html_node(markdown)
        result = HTMLNode(children=[ParentNode(tag="h3", children=[LeafNode(value="This is a heading")]),
                                    ParentNode(tag="pre", children=[ParentNode(tag="code", children=[LeafNode(value="This is a paragraph of text. It has some "),
                                                                                                    LeafNode("b", "bold"),
                                                                                                    LeafNode(value=" and "),
                                                                                                    LeafNode("i", "italic"),
                                                                                                    LeafNode(value=" words inside of it.")])]),
                                    ParentNode(tag="ol", children=[ParentNode("li", children=[LeafNode(value="This is the first "),
                                                                                              LeafNode('i', "list"),
                                                                                              LeafNode(value=" item in a list block")]),
                                                                    ParentNode("li", children=[LeafNode(value="This is a list item")]),
                                                                    ParentNode("li", children=[LeafNode(value="This is another list item")])])]
        )
        
        assert html_node.__repr__() == result.__repr__()
        assert html_node.children[0].to_html() == result.children[0].to_html()
        assert html_node.children[1].to_html() == result.children[1].to_html()
        assert html_node.children[2].to_html() == result.children[2].to_html()

if __name__ == "__main__":
    unittest.main()