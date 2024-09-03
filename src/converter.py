from enum import Enum
from leafnode import LeafNode


#class Text_Type(Enum):
#    text_type_text = "text"
#    text_type_bold = "bold"
#    text_type_italic = "italic"
#    text_type_code = "code"
#    text_type_link = "link"
#    text_type_image = "image"
#
#def text_node_to_html_node(text_node):
#    match text_node.text_type:
#        case Text_Type.text_type_text.value:
#            return LeafNode(value=text_node.text)
#        case Text_Type.text_type_bold.value:
#            return LeafNode(tag='b', value=text_node.text)
#        case Text_Type.text_type_italic.value:
#            return LeafNode(tag='i', value=text_node.text)
#        case Text_Type.text_type_code.value:
#            return LeafNode(tag='code', value=text_node.text)
#        case Text_Type.text_type_link.value:
#            return LeafNode(tag='a', value=text_node.text, props={'hrefs': text_node.url})
#        case Text_Type.text_type_image.value:
#            return LeafNode(tag='img', value='', props={'src': text_node.url, 'alt': text_node.text})
#        case _:
#            raise Exception("Unexpected Text Type")

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode(value=text_node.text)
        case "bold":
            return LeafNode(tag='b', value=text_node.text)
        case "italic":
            return LeafNode(tag='i', value=text_node.text)
        case "code":
            return LeafNode(tag='code', value=text_node.text)
        case "link":
            return LeafNode(tag='a', value=text_node.text, props={'hrefs': text_node.url})
        case "image":
            return LeafNode(tag='img', value='', props={'src': text_node.url, 'alt': text_node.text})
        case _:
            raise Exception("Unexpected Text Type")