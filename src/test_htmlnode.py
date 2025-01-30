import unittest

from htmlnode import *

class TestHtmlNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode("tag_prova", "Ciaociaociao",None ,{"uno": "pippo", "due": "pluto"})
 #       node.to_html()

    def test_props(self):
        node = HTMLNode("tag_prova", "Ciaociaociao",None ,{"uno": "pippo", "due": "pluto"})
        print("test props")
        print(node.props_to_html())

    def test_repr(self):
        node = HTMLNode("tag_prova", "Ciaociaociao",None ,{"uno": "pippo", "due": "pluto"})
        print("test repr")
        print(node.__repr__())

if __name__ == "__main__":
    unittest.main()
