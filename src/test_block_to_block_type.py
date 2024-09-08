import unittest

from helper_functions import block_to_block_type


class TestMarkdownToBlocks(unittest.TestCase):
    def test_headings(self):
        block = "##### This is a heading"
        block_paragraph = "######## This should be a paragraph"
        block_paragraph2 = "#This should be a paragraph too"

        assert block_to_block_type(block) == "heading"
        assert block_to_block_type(block_paragraph) == "paragraph"
        assert block_to_block_type(block_paragraph2) == "paragraph"
        
    def test_code(self):
        code_block = "```This is a code block indeed\nYes```"
        block_paragraph = "```This is not a code block```hi"

        assert block_to_block_type(code_block) == "code"
        assert block_to_block_type(block_paragraph) == "paragraph"

    def test_quote(self):
        quote_block = "> Why hello there"

        assert block_to_block_type(quote_block) == "quote"

    def test_unordered_list(self):
        unordered_list_block = "* first\n- second\n* third"
        block_paragraph = "* first\n - second"
        block_paragraph_2 = "*first\n- second"

        assert block_to_block_type(unordered_list_block) == "unordered_list"
        assert block_to_block_type(block_paragraph) == "paragraph"
        assert block_to_block_type(block_paragraph_2) == "paragraph"

    def test_ordered_list(self):
        ordered_list_block = "1. first\n2. second\n3. third"
        block_paragraph = "1 first\n2. second"
        block_paragraph_2 = "3. first\n1. second"
        block_paragraph_3 = "1. first\n3. second"
        block_paragraph_4 = " 1. first\n2. second"

        assert block_to_block_type(ordered_list_block) == "ordered_list"
        assert block_to_block_type(block_paragraph) == "paragraph"
        assert block_to_block_type(block_paragraph_2) == "paragraph"
        assert block_to_block_type(block_paragraph_3) == "paragraph"
        assert block_to_block_type(block_paragraph_4) == "paragraph"

if __name__ == "__main__":
    unittest.main()