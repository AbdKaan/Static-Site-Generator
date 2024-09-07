import re
from textnode import TextNode


def split_nodes_delimiter(old_nodes, delimiter=None, text_type=None):
    text_nodes = []

    for node in old_nodes:
        if node.text_type != TextNode.text_type_text:
            text_nodes.append(node)
        else:
            if node.text.count(delimiter) % 2 != 0:
                print(delimiter)
                print(node.text.count(delimiter))
                print(node.text)
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