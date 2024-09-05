import unittest

from helper_functions import split_nodes_image, split_nodes_link
from textnode import TextNode


class TestSplitNodes(unittest.TestCase):
    def test_image_split(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKa0qIh.gif)!", TextNode.text_type_text)
        nodes = split_nodes_image([node])
        result_text = TextNode("This is text with a ", TextNode.text_type_text)
        result_image = TextNode("rick roll", TextNode.text_type_image, "https://i.imgur.com/aKa0qIh.gif")
        result_text_two = TextNode("!", TextNode.text_type_text)
        assert nodes[0] == result_text and nodes[1] == result_image and nodes[2] == result_text_two

    def test_link_split(self):
        node = TextNode("This is text with a [rick roll](https://i.imgur.com/aKa0qIh.gif)!", TextNode.text_type_text)
        nodes = split_nodes_link([node])
        result_text = TextNode("This is text with a ", TextNode.text_type_text)
        result_link = TextNode("rick roll", TextNode.text_type_link, "https://i.imgur.com/aKa0qIh.gif")
        result_text_two = TextNode("!", TextNode.text_type_text)
        assert nodes[0] == result_text and nodes[1] == result_link and nodes[2] == result_text_two

    def test_no_space_between_two_links(self):
        node = TextNode("Testing [best website](boot.dev)[obi wan](obiwan.com)", TextNode.text_type_text)
        link_markdown = split_nodes_link([node])
        result_text = TextNode("Testing ", TextNode.text_type_text)
        result_link = TextNode("best website", TextNode.text_type_link, "boot.dev")
        result_link2 = TextNode("obi wan", TextNode.text_type_link, "obiwan.com")
        assert link_markdown[0] == result_text and link_markdown[1] == result_link and link_markdown[2] == result_link2

    def test_three_links(self):
        node = TextNode("Testing [best website](boot.dev) and [obi wan](obiwan.com) and ofc [gandalf](youshallnotpass.lotr)", TextNode.text_type_text)
        link_markdown = split_nodes_link([node])
        result_text = TextNode("Testing ", TextNode.text_type_text)
        result_link = TextNode("best website", TextNode.text_type_link, "boot.dev")
        result_text2 = TextNode(" and ", TextNode.text_type_text)
        result_link2 = TextNode("obi wan", TextNode.text_type_link, "obiwan.com")
        result_text3 = TextNode(" and ofc ", TextNode.text_type_text)
        result_link3 = TextNode("gandalf", TextNode.text_type_link, "youshallnotpass.lotr")
        assert (link_markdown[0] == result_text
                and link_markdown[1] == result_link
                and link_markdown[2] == result_text2
                and link_markdown[3] == result_link2
                and link_markdown[4] == result_text3
                and link_markdown[5] == result_link3)

    def test_starting_with_link(self):
        node = TextNode("[youtube](youtube.com) is a great website.", TextNode.text_type_text)
        nodes = split_nodes_link([node])
        result_link = TextNode("youtube", TextNode.text_type_link, "youtube.com")
        result_text = TextNode(" is a great website.", TextNode.text_type_text)
        assert nodes[0] == result_link and nodes[1] == result_text

    def test_ending_with_link(self):
        node = TextNode("A great website is [youtube](youtube.com)", TextNode.text_type_text)
        nodes = split_nodes_link([node])
        result_text = TextNode("A great website is ", TextNode.text_type_text)
        result_link = TextNode("youtube", TextNode.text_type_link, "youtube.com")
        assert nodes[0] == result_text and nodes[1] == result_link

    def test_no_links(self):
        node = TextNode("Stop using internet.", TextNode.text_type_text)
        nodes = split_nodes_link([node])
        assert nodes[0] == node

    def test_multiple_nodes(self):
        node1 = TextNode("A great website is [youtube](youtube.com)", TextNode.text_type_text)
        node2 = TextNode("[youtube](youtube.com) is a great website.", TextNode.text_type_text)
        nodes = split_nodes_link([node1, node2])
        result_text = TextNode("A great website is ", TextNode.text_type_text)
        result_link = TextNode("youtube", TextNode.text_type_link, "youtube.com")
        result_link2 = TextNode("youtube", TextNode.text_type_link, "youtube.com")
        result_text2 = TextNode(" is a great website.", TextNode.text_type_text)
        assert (nodes[0] == result_text and
                nodes[1] == result_link and
                nodes[2] == result_link2 and
                nodes[3] == result_text2)

if __name__ == "__main__":
    unittest.main()