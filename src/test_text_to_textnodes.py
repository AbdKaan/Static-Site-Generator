import unittest

from helper_functions import text_to_textnodes
from textnode import TextNode


class TestTextToTextNodes(unittest.TestCase):
    def test(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        result = [
            TextNode("This is ", TextNode.text_type_text),
            TextNode("text", TextNode.text_type_bold),
            TextNode(" with an ", TextNode.text_type_text),
            TextNode("italic", TextNode.text_type_italic),
            TextNode(" word and a ", TextNode.text_type_text),
            TextNode("code block", TextNode.text_type_code),
            TextNode(" and an ", TextNode.text_type_text),
            TextNode("obi wan image", TextNode.text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextNode.text_type_text),
            TextNode("link", TextNode.text_type_link, "https://boot.dev"),
        ]

        assert nodes == result

    def test2(self):
        text = "**This is** **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        result = [
            TextNode("This is", TextNode.text_type_bold),
            TextNode(" ", TextNode.text_type_text),
            TextNode("text", TextNode.text_type_bold),
            TextNode(" with an ", TextNode.text_type_text),
            TextNode("italic", TextNode.text_type_italic),
            TextNode(" word and a ", TextNode.text_type_text),
            TextNode("code block", TextNode.text_type_code),
            TextNode(" and an ", TextNode.text_type_text),
            TextNode("obi wan image", TextNode.text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextNode.text_type_text),
            TextNode("link", TextNode.text_type_link, "https://boot.dev"),
        ]

        assert nodes == result

    def test3(self):
        text = "This is **text** with an *italic* word, an image: ![rick roll](rickroll.gif) and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        result = [
            TextNode("This is ", TextNode.text_type_text),
            TextNode("text", TextNode.text_type_bold),
            TextNode(" with an ", TextNode.text_type_text),
            TextNode("italic", TextNode.text_type_italic),
            TextNode(" word, an image: ", TextNode.text_type_text),
            TextNode("rick roll", TextNode.text_type_image, "rickroll.gif"),
            TextNode(" and a ", TextNode.text_type_text),
            TextNode("code block", TextNode.text_type_code),
            TextNode(" and an ", TextNode.text_type_text),
            TextNode("obi wan image", TextNode.text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextNode.text_type_text),
            TextNode("link", TextNode.text_type_link, "https://boot.dev"),
        ]

        assert nodes == result

if __name__ == "__main__":
    unittest.main()