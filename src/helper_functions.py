import re
from textnode import TextNode
from leafnode import LeafNode
from parentnode import ParentNode
from htmlnode import HTMLNode


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
            return LeafNode(tag='a', value=text_node.text, props={'href': text_node.url})
        case TextNode.text_type_image:
            return LeafNode(tag='img', value='', props={'src': text_node.url, 'alt': text_node.text})
        case _:
            raise Exception("Unexpected Text Type")

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

def extract_markdown_images(text):
    # Example: ![rick roll](https://i.imgur.com/aKaOqIh.gif) -> ("rick roll", "https://i.imgur.com/aKaOqIh.gif")
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    # Example: [to boot dev](https://www.boot.dev) -> ("to boot dev", "https://www.boot.dev")
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        images = extract_markdown_images(node.text)

        if images == []:
            new_nodes.append(node)
            continue

        text = node.text
        len_images = len(images)
        idx = 1
        for image in images:
            sections = text.split(f"![{image[0]}]({image[1]})", 1)
            if sections[0] != '':
                new_nodes.append(TextNode(sections[0], TextNode.text_type_text))
            new_nodes.append(TextNode(image[0], TextNode.text_type_image, image[1]))
            if idx == len_images and sections[1] != '':
                new_nodes.append(TextNode(sections[1], TextNode.text_type_text))
            else:
                text = sections[1]
                idx += 1

    return new_nodes
        
def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        links = extract_markdown_links(node.text)

        if links == []:
            new_nodes.append(node)
            continue

        text = node.text
        len_links = len(links)
        idx = 1
        for link in links:
            sections = text.split(f"[{link[0]}]({link[1]})", 1)
            if sections[0] != '':
                new_nodes.append(TextNode(sections[0], TextNode.text_type_text))
            new_nodes.append(TextNode(link[0], TextNode.text_type_link, link[1]))
            if idx == len_links and sections[1] != '':
                new_nodes.append(TextNode(sections[1], TextNode.text_type_text))
            else:
                text = sections[1]
                idx += 1

    return new_nodes

def text_to_textnodes(text):
    node = TextNode(text, TextNode.text_type_text)
    nodes = [node]
    text_types_for_delimiter = [(TextNode.text_type_bold, "**"),
                                (TextNode.text_type_code, "`"),
                                (TextNode.text_type_italic, "*")]
    for text_type in text_types_for_delimiter:
        nodes = split_nodes_delimiter(nodes, text_type[1], text_type[0])
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return blocks

def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return "heading"
    elif block[:3] == "```" and block[-3:] == "```":
        return "code"
    elif block[0] == '>':
        return "quote"
    elif block[:2] == "* " or block[:2] == "- ":
        for line in block.split("\n"):
            if not (line[:2] == "* " or line[:2] == "- "):
                return "paragraph"
        return "unordered_list"
    elif block.split(". ")[0] == "1":
        row = 1
        for line in block.split("\n"):
            if line.split(". ")[0] == f"{row}":
                row += 1
            else:
                return "paragraph"
        return "ordered_list"
    else:
        return "paragraph"

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    leaf_nodes = []
    for node in text_nodes:
        leaf_nodes.append(text_node_to_html_node(node))
    return leaf_nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    main_children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == "heading":
            split_block = block.split(" ", 1)
            header_size = len(split_block[0])
            parent_node = ParentNode(f"h{header_size}", children=text_to_children(split_block[1]))
        elif block_type == "code":
            code_node = ParentNode("code", children=text_to_children(block[3:-3].split("\n", 1)[1]))
            parent_node = ParentNode("pre", children=[code_node])
        elif block_type == "quote":
            parent_node = ParentNode("blockquote", children=text_to_children(block[2:]))
        elif block_type == "unordered_list":
            children = []
            for node in block.split("\n"):
                parent_list_item_node = ParentNode("li", children=text_to_children(node[2:]))
                children.append(parent_list_item_node)
            parent_node = ParentNode("ul", children=children)
        elif block_type == "ordered_list":
            children = []
            for node in block.split("\n"):
                parent_list_item_node = ParentNode("li", children=text_to_children(node[3:]))
                children.append(parent_list_item_node)
            parent_node = ParentNode("ol", children=children)
        elif block_type == "paragraph":
            parent_node = ParentNode("p", children=text_to_children(block))

        main_children.append(parent_node)

    return ParentNode("div", children=main_children)