from functools import reduce
from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props={}):
        # Children needs to exist
        if children == None or children == []:
            raise ValueError("Children can't be empty")

        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None or self.tag == "":
            raise ValueError("Tag is empty")

        if self.children == None:
            raise ValueError("Children can't be empty")

        return f'<{self.tag}{self.props_to_html()}>{reduce(lambda x, y: x + y.to_html(), self.children, "")}</{self.tag}>'