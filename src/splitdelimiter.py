from textnode import * 
from extractmarkdown import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL or delimiter not in old_node.text:
            text_nodes.extend([old_node])
        else:
            node = old_node.text.split(delimiter)
            text_nodes.extend(
                [
                    TextNode(node[0], TextType.NORMAL),
                    TextNode(node[1], text_type),
                    TextNode(node[2], TextType.NORMAL)
                    ])

    return text_nodes

def split_nodes_image(old_nodes):
    def extract(old_node):
        matches = extract_markdown_images(old_node.text)
        if matches == []:
            return [old_node]
        else:
            splitted = old_node.text.split(f"![{matches[0][0]}]({matches[0][1]})", maxsplit=1)
            out = [
                    TextNode(splitted[0], old_node.text_type),
                    TextNode(matches[0][0], TextType.IMAGE, matches[0][1])
                ]
            if splitted[1] != "":
                out.extend(
                    split_nodes_image([TextNode(splitted[1], old_node.text_type)])
                )
            return out

    new_nodes = []
    for old_node in old_nodes:
        new_nodes.extend(extract(old_node))
    return new_nodes

def split_nodes_link(old_nodes):
    def extract(old_node):
        matches = extract_markdown_links(old_node.text)

        if matches == []:
            return [old_node]
        else:
            splitted = old_node.text.split(f"[{matches[0][0]}]({matches[0][1]})", maxsplit=1)
            out = [
                    TextNode(splitted[0], old_node.text_type),
                    TextNode(matches[0][0], TextType.LINK, matches[0][1])
                ]
            if splitted[1] != "":
                out.extend(
                    split_nodes_link([TextNode(splitted[1], old_node.text_type)])
                )
            return out
        
    new_nodes = []    
    for old_node in old_nodes:
        new_nodes.extend(extract(old_node))
    return new_nodes
        