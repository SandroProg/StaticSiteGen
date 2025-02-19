import unittest

from markdowntohtml import *

class TestHtmlNode(unittest.TestCase):

    def test_markdown_to_html_node(self):
        text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        print("\n\nMARKDOWN TO HTML TEST\n")
        print(markdown_to_html_node(text))


if __name__ == "__main__":
    unittest.main()
