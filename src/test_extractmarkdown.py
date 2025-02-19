import unittest

from extractmarkdown import *

class TestHtmlNode(unittest.TestCase):
    '''
    def test_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        print("\n\nMARKDOWN TO IMAGES TEST\n")
        print(extract_markdown_images(text))


    def test_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        print("\n\nMARKDOWN TO LINK TEST\n")
        print(extract_markdown_links(text))

    def test_extract_markdown(self):
        text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n\n\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n"
        print("\n\nMARKDOWN TO BLOCKS\n")
        print(markdown_to_blocks(text))

    def test_paragraph_block(self):
        block = "Ciao ciao babbo\n* non è un elenco 2 3 \n\nCiao"
        print("\n\nPARAGRAPH TEST\n")
        print(block_to_block_type(block))

    def test_heading_block(self):
        block = "### Questo è un titolo"
        print("\n\nHEADING BLOCK TEST\n")
        print(block_to_block_type(block))

    def test_code_block(self):
        block = "```print('ciao mondo')\n\nmain()```"
        print("\n\nCODE_BLOCK_TEST\n")
        print(block_to_block_type(block))

    def test_quote_block(self):
        block = ">Quent'è bella giovinezza\n>che si fugge tuttavia\n>chi vuol esser lieto sia\n>del diman non v'è certezza"
        print("\n\nQUOTE_BLOCK_TEST\n")
        print(block_to_block_type(block))

    def test_unordered_block(self):
        block = "* farina\n* zucchero\n* margarina"
        print("\n\nUNORDERED LIST BLOCK TEST\n")
        print(block_to_block_type(block))

    def test_ordered_block(self):
        block = "1. mescolare gli ingredienti\n2. stendere su una teglia\n3. infornare"
        print("\n\nORDERED LIST BLOCK TEST")
        print(block_to_block_type(block))
        '''


if __name__ == "__main__":
    unittest.main()
