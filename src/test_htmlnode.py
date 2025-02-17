import unittest

from htmlnode import *

class TestHtmlNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode("tag_prova", "Ciaociaociao",None ,{"uno": "pippo", "due": "pluto"})
 #       node.to_html()

    def test_props(self):
        node = HTMLNode("tag_prova", "Ciaociaociao",None ,{"uno": "pippo", "due": "pluto"})
        print("\n\ntest props\n")
        print(node.props_to_html())

    def test_repr(self):
        node = HTMLNode("tag_prova", "Ciaociaociao",None ,{"uno": "pippo", "due": "pluto"})
        print("\n\ntest repr\n")
        print(node.__repr__())

    def test_leafnode(self):
        node = LeafNode("p", "This is a paragraph of text.")
        print("\n\ntest LeafNode\n")
        print(node.to_html())

    def test_leaf_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        print("\n\ntest to html\n")
        print(node.to_html())

    def test_parent1(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        
        print("\n\ntest parent node 1\n")
        print(node.to_html())

    def test_parent2(self):
        node = ParentNode("p", [ParentNode("p", [LeafNode("b", "Bold text"), LeafNode("i", "italic text")])])
        print("\n\ntest parent node 2\n")
        print(node.to_html())

    def test_text_to_html1(self):
        node = TextNode("QUESTO è IL TESTO", TextType.ITALIC)
        print(f"\n\nTEST: TEXT TO HTML 1\n\n")
        print(text_node_to_html_node(node))
                        
    def test_text_to_html2(self):
        node = TextNode(None, TextType.IMAGE, "http:\\www.ciao.it")
        print(f"\n\nTEST: TEXT TO HTML 2\n\n")
        print(text_node_to_html_node(node))


if __name__ == "__main__":
    unittest.main()
