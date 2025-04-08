import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_different_text(self):
        node = TextNode("This is a text node", TextType.ITALIC, "www.boot.dev")
        node2 = TextNode("This is not a text node", TextType.ITALIC, "www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_not_equal_different_type(self):
        node = TextNode("Text node", TextType.NORMAL, "www.boot.dev")
        node2 = TextNode("Text node", TextType.CODE, "www.boot.dev")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
