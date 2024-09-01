import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode(tag="p", value="Test paragraph",  props={"class": "test-class"})
        assert node.to_html() == '<p class="test-class">Test paragraph</p>'

    def test_no_tag(self):
        node = LeafNode(tag="", value="You shall not pass!", props={"Why": "??"})
        assert node.to_html() == "You shall not pass!"

    def test_value(self):
        node = LeafNode(tag="p", value="Test paragraph", props={"class": "test-class"})
        assert node.value != None

    def test_children(self):
        node = LeafNode(tag='a', value='somelink')
        assert node.children == None

if __name__ == "__main__":
    unittest.main()