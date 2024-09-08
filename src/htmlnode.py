class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = {}):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        return "".join([f' {key}="{value}"' for key, value in self.props.items()])

    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nChildren:\n{self.children}\nProps: {self.props}"