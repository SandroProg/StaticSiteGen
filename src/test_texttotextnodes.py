import unittest

from texttotextnodes import *

class TestSplitDelimiter(unittest.TestCase):
    def test_text_to_nodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        print("\n\nTEXT TO NODE TEST\n")
        print(text_to_textnode(text))

    def test_text_to_nodes_2(self):
        text = ""
        print("\n\nTEXT (VOID) TO NODE TEST\n")
        print(text_to_textnode(text))