class TextNode():
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, textnode):
        # Compare with another TextNode instance
        if self.text == textnode.text and self.text_type == textnode.text_type and self.url == textnode.url:
            return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"