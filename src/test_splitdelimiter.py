import unittest

from splitdelimiter import *

class TestSplitDelimiter(unittest.TestCase):
    def test_split_1(self):
        old_nodes = [
            TextNode("Testo a **caso**", TextType.NORMAL),
            TextNode("NON URLARE", TextType.BOLD),
            TextNode("possiamo *finirla* qui, va", TextType.NORMAL)
        ]
        print("\n\nTEST SPLIT 1\n\n")
        print(split_nodes_delimiter(old_nodes, "**", TextType.BOLD))

    def test_split_2(self):
        old_nodes = [
            TextNode("Testo a **caso**", TextType.NORMAL),
            TextNode("NON URLARE", TextType.BOLD),
            TextNode("possiamo *finirla* qui, va", TextType.NORMAL)
        ]
        print("\n\nTEST SPLIT 2\n\n")
        print(split_nodes_delimiter(old_nodes, "*", TextType.ITALIC))

    def test_split_nodes_image(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.NORMAL)
        print("\n\nSPLIT NODES IMAGES TEST 1\n")
        print(split_nodes_image([node]))

    def test_split_nodes_image_2(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL)
        print("\n\nSPLIT NODES IMAGES TEST 2\n")
        print(split_nodes_image([node]))

    def test_split_nodes_image_3(self):
        node = TextNode("", TextType.NORMAL)
        print("\n\nSPLIT NODES IMAGES TEST 3\n")
        print(split_nodes_image([node]))

    def test_split_nodes_link(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.NORMAL)
        print("\n\nSPLIT NODES LINK TEST 1\n")
        print(split_nodes_link([node]))

    def test_split_nodes_link_2(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL)
        print("\n\nSPLIT NODES LINK TEST 2\n")
        print(split_nodes_link([node]))

if __name__ == "__main__":
    unittest.main()