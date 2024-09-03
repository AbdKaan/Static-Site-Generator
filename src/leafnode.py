from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, props: dict = {}):
        # Value needs to exist
        if value == None:
            raise ValueError("There needs to be some value.")

        # Can't have child, children=None
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError()
        
        if self.tag == None or self.tag == "":
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"