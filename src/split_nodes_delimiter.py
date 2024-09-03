from textnode import TextNode


def split_nodes_delimiter(old_nodes, delimiter=None, text_type=None):
    text_nodes = []

    for node in old_nodes:
        if node.text_type != TextNode.text_type_text:
            text_nodes.append(node)
        else:
            if node.text.count(delimiter) % 2 != 0:
                raise Exception("Invalid Markdown Syntax")

            nodes = node.text.split(delimiter)
            for idx, text in enumerate(nodes):
                if idx % 2 == 0:
                    text_nodes.append(TextNode(text, TextNode.text_type_text))
                else:
                    text_nodes.append(TextNode(text, text_type))
        if text_nodes[0].text == "":
            del[text_nodes[0]]
        elif text_nodes[-1].text == "":
            del[text_nodes[-1]]


    return text_nodes