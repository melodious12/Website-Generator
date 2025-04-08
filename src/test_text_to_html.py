import unittest

from text_to_html import text_node_to_html_node

from textnode import TextNode, TextType

from htmlnode import LeafNode

class TestTexttoHtml(unittest.TestCase):
    def test_normal_text(self):
        node = TextNode("normal text", TextType.NORMAL)
        self.assertEqual(LeafNode(None, "normal text"), text_node_to_html_node(node))
    def test_bold_text(self):
        node = TextNode("bold text", TextType.BOLD)
        self.assertEqual(LeafNode("b", "bold text"), text_node_to_html_node(node))
    def test_italic_text(self):
        node = TextNode("italic text", TextType.ITALIC)
        self.assertEqual(LeafNode("i", "italic text"), text_node_to_html_node(node))
    def test_code_text(self):
        node = TextNode("code text", TextType.CODE)
        self.assertEqual(LeafNode("code", "code text"), text_node_to_html_node(node))
    def test_link_text(self):
        node = TextNode("link text", TextType.LINK, "www.link.com")
        self.assertEqual(LeafNode("a", "link text", {"href": "www.link.com"}), text_node_to_html_node(node))
    def test_image_text(self):
        node = TextNode("image text", TextType.IMAGE, "www.image.com")
        self.assertEqual(LeafNode("img", "", {"src": "www.image.com", "alt": "image text"}), text_node_to_html_node(node))
    def test_wrong_text_type(self):
        node = TextNode("test text", TextType.NORMAL)
        node.text_type = "invalid"
        with self.assertRaises(Exception):
            text_node_to_html_node(node)
