from texttotextnodes import *
from extractmarkdown import *

def block_to_block_type(block):
    header = 0
    for i in range(0, 6):
        if block[i] != "#":
            break
        header = i + 1
    if header != 0:
        return "heading", header

    if block[0:3] == "```" and block[-3:] == "```":
        return "code", 0
    
    splitted = block.splitlines()
    
    check_quote = True
    for line in splitted:
        check_quote = check_quote and (line[0] == ">")
    if check_quote:
        return "quote", 0
    
    check_ulist = True
    for line in splitted:
        check_ulist = check_ulist and (line[0]=="*" or line[0]=="-") and line[1]==" "
    if check_ulist:
        return "unordered_list", 0

    if isinstance(splitted, list):
        check_olist = True
        for i in range(0, len(splitted)):
            check_olist = check_olist and splitted[i][0:len(str(i))] == str(i+1) and splitted[i][len(str(i+1)):len(str(i+1))+2] == ". "
        
        if check_olist:
            return "ordered_list", 0
        
    return "paragraph", 0

def text_to_children(text):
    nodes = text_to_textnode(text)
    children = []
    for node in nodes:
        children.append(text_node_to_html_node(node))
    return children

def markdown_to_html_node(markdown):
    
    block_list = markdown_to_blocks(markdown)

    children = []

    for block in block_list:
        block_type, header = block_to_block_type(block)
        match block_type:
            case "heading":
                child = ParentNode(f"h{header}",text_to_children(block[header:]))

            case "code":
                child = ParentNode("pre", LeafNode("code", block[3:-3]))

            case "quote":
                child = ParentNode("blockquote",text_to_children(block))
            
            case "unordered_list":
                splitted = block.splitlines(keepends=True).lstrip("* ").lstrip("- ")
                lines = list(map(lambda line: ParentNode("li", text_to_children(line)), splitted))
                child = ParentNode("ul", lines)

            case "ordered_list":
                splitted = block.splitlines(keepends=True)
                lines = list(map(lambda line: ParentNode("li", text_to_children(line)), splitted))
                child = ParentNode("ol", lines)

            case "paragraph":
                child = ParentNode("p", text_to_children(block))
        
        children.append(child)
    
    return ParentNode("div", children)
