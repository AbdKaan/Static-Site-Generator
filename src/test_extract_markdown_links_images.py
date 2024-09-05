import unittest

from helper_functions import extract_markdown_images, extract_markdown_links


class TestExtractMarkdownLinksImages(unittest.TestCase):
    def test_image_extraction(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        image_markdown = extract_markdown_images(text)
        result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        assert image_markdown == result

    def test_link_extraction(self):
        text = "This is [lmao](www.lmao.com) text with a [rick roll](https://i.imgur.com/aKaOqIh.gif)"
        link_markdown = extract_markdown_links(text)
        result = [("lmao", "www.lmao.com"), ("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        assert link_markdown == result

    def test_link_extraction_with_image(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        link_markdown = extract_markdown_links(text)
        result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        assert link_markdown == result

if __name__ == "__main__":
    unittest.main()