from textnode import *

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        out = ""
        for key in self.props:
            out += ' ' + key + '="' + self.props[key] + '"'

        return out
    
    def __repr__(self):
        out = f"tag = {self.tag}\n"
        out += f"value = {self.value}\n"
        out += f"children = {self.children}\n"
        out += f"props = {self.props}"
        return out

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        match self.tag:
            case "p":
                return f"<p>{self.value}</p>"
            case "b":
                return f"<b>{self.value}</b>"
            case "i":
                return f"<i>{self.value}</i>"
            case "a":
                return f"<a{self.props_to_html()}>{self.value}</a>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent tag missing")
        if self.children == None:
            raise ValueError("Parent children missing")
        return "<" + self.tag + ">" + "".join(list(map(lambda x: x.to_html(), self.children))) + "</" + self.tag + ">"
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(None, text_node.text)
        
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": ""})
            