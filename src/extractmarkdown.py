import re

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return list(map(lambda s: s.strip("\n").strip(" "), list(filter(lambda x: x != "", blocks))))

def block_to_block_type(block):
    header = 0
    for i in range(0, 6):
        if block[i] != "#":
            break
        header = i + 1
    if header != 0:
        return "heading"

    if block[0:3] == "```" and block[-3:] == "```":
        return "code"
    
    splitted = block.splitlines()
    
    check_quote = True
    for line in splitted:
        check_quote = check_quote and (line[0] == ">")
    if check_quote:
        return "quote"
    
    check_ulist = True
    for line in splitted:
        check_ulist = check_ulist and (line[0]=="*" or line[0]=="-") and line[1]==" "
    if check_ulist:
        return "unordered_list"

    if isinstance(splitted, list):
        check_olist = True
        for i in range(0, len(splitted)):
            check_olist = check_olist and splitted[i][0:len(str(i))] == str(i+1) and splitted[i][len(str(i+1)):len(str(i+1))+2] == ". "
        
        if check_olist:
            return "ordered_list"
        
    return "paragraph"