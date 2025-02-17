from textnode import *
from htmlnode import *

def main():
    obj = TextNode("ciao", TextType.BOLD, "https://www.boot.dev")
    print(obj.__repr__)

main()
