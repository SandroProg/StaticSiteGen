import re
from htmlnode import *

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return list(map(lambda s: s.strip("\n").strip(" "), list(filter(lambda x: x != "", blocks))))

