class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        strings = []
        if self.props is None or len(self.props) <= 0:
            return ""
        for key, value in self.props.items():
            strings.append(f' {key}="{value}"')
        return "".join(strings)

    def __repr__(self):
        parts = []
        if self.tag is not None:
            parts.append(f'tag="{self.tag}"')
        if self.value is not None:
            parts.append(f'value="{self.value}"')
        if self.children is not None:
            parts.append(f'children={self.children}')
        if self.props is not None:
            parts.append(f'props={self.props}')
        return f"HTMLNode({', '.join(parts)})"

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag == other.tag and 
                self.value == other.value and 
                self.props == other.props)

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError
        if self.children == None:
            raise ValueError("missing children")
        parent_list = []
        parent_list.append(f"<{self.tag}{self.props_to_html()}>")
        for child in self.children:
            parent_list.append(child.to_html())
        parent_list.append(f"</{self.tag}>")
        return "".join(parent_list)
