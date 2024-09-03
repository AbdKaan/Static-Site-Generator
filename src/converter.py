from leafnode import LeafNode
from textnode import TextNode


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextNode.text_type_text:
            return LeafNode(value=text_node.text)
        case TextNode.text_type_bold:
            return LeafNode(tag='b', value=text_node.text)
        case TextNode.text_type_italic:
            return LeafNode(tag='i', value=text_node.text)
        case TextNode.text_type_code:
            return LeafNode(tag='code', value=text_node.text)
        case TextNode.text_type_link:
            return LeafNode(tag='a', value=text_node.text, props={'hrefs': text_node.url})
        case TextNode.text_type_image:
            return LeafNode(tag='img', value='', props={'src': text_node.url, 'alt': text_node.text})
        case _:
            raise Exception("Unexpected Text Type")