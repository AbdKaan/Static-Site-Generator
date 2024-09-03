import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_props(self):
        leaf1 = LeafNode("p", "Great paragraph", {"class": "this"})
        parent_node = ParentNode(tag="span", children=[leaf1], props={"style": "color:#ffffff"})
        parent_node_no_prop = ParentNode(tag="span", children=[leaf1])
        assert parent_node.to_html() == '<span style="color:#ffffff"><p class="this">Great paragraph</p></span>'
        assert parent_node_no_prop.to_html() == '<span><p class="this">Great paragraph</p></span>'

    def test_just_leaf_nodes(self):
        leaf1 = LeafNode("p", "Great paragraph", {"class": "this"})
        leaf2 = LeafNode("p", "leaf2", {"class": "class2"})
        leaf3 = LeafNode("p", "leaf3", {"class": "class3", "style": 'margin:0;'})
        parent_node = ParentNode(tag="table", children=[leaf1, leaf2, leaf3], props={})
        assert parent_node.to_html() == '<table><p class="this">Great paragraph</p><p class="class2">leaf2</p><p class="class3" style="margin:0;">leaf3</p></table>'

    def test_nested_parent_nodes(self):
        leaf1 = LeafNode("p", "leaf1", {"class": "class1"})
        leaf2 = LeafNode("p", "leaf2", {"class": "class2"})
        parent_node1 = ParentNode(tag="div", children=[leaf1, leaf2], props={})
        parent_node2 = ParentNode(tag="div", children=[parent_node1], props={})
        assert parent_node2.to_html() == '<div><div><p class="class1">leaf1</p><p class="class2">leaf2</p></div></div>'

    def test_nested_nested_parent_nodes(self):
        leaf1 = LeafNode("p", "leaf1", {"class": "class1"})
        leaf2 = LeafNode("p", "leaf2", {"class": "class2"})
        parent_node1 = ParentNode(tag="div", children=[leaf1, leaf2], props={})
        leaf3 = LeafNode("p", "leaf3", {"class": "class3"})
        parent_node2 = ParentNode(tag="div", children=[parent_node1, leaf3], props={})
        parent_node3 = ParentNode(tag="div", children=[parent_node2], props={"id": "id1"})
        assert parent_node3.to_html() == '<div id="id1"><div><div><p class="class1">leaf1</p><p class="class2">leaf2</p></div><p class="class3">leaf3</p></div></div>'

if __name__ == "__main__":
    unittest.main()