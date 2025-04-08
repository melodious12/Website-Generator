import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_empty_props(self):
        node = HTMLNode(tag="p")
        self.assertEqual(node.props_to_html(), "")

    def test_single_prop(self):
        node = HTMLNode(tag="a", value="some text", props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_mult_props(self):
        node = HTMLNode(tag="p", props={"href": "link.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="link.com" target="_blank"')

    def test_basic_leaf_node(self):
        node = LeafNode("p", "This is a paragraph")
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")

    def test_no_tag_leaf(self):
        node = LeafNode(tag=None, value="Test text")
        self.assertEqual(node.to_html(), "Test text")

    def test_leaf_with_prop(self):
        node = LeafNode(tag="a", value="Hello", props={"href": "www.hello.com"})
        self.assertEqual(node.to_html(), '<a href="www.hello.com">Hello</a>')

    def test_leaf_no_value(self):
        node = LeafNode(tag="p", value=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_no_child(self):
        node = ParentNode(tag="p", children=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_no_tag(self):
        node = ParentNode(tag=None, children=LeafNode("b", "Bold text"))
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_mult_children(self):
        node = ParentNode(
            "div",
            [
                LeafNode("p", "First child"),
                LeafNode("p", "Second child"),
                LeafNode("p", "Third child")
            ]
        )
        self.assertEqual(node.to_html(), "<div><p>First child</p><p>Second child</p><p>Third child</p></div>")

    def test_parent_leaf_mix_tags(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_mult_parents(self):
        node = ParentNode(
            "div",
            [
                LeafNode("p", "First paragraph"),
                ParentNode(
                    "section",
                    [
                        LeafNode("h1", "Title"),
                        LeafNode("p", "Some text")
                    ]
                ),
                LeafNode("p", "Last paragraph")
            ]
        )
        self.assertEqual(node.to_html(), "<div><p>First paragraph</p><section><h1>Title</h1><p>Some text</p></section><p>Last paragraph</p></div>")

if __name__ == "__main__":
    unittest.main()
