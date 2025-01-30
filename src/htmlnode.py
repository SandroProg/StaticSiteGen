class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        out = ""
        for key in self.props:
            out += ' ' + key + '="' + self.props[key] + '"'

        return out
    
    def __repr__(self):
        out = f"tag = {self.tag}\n"
        out += f"value = {self.value}\n"
        out += f"children = {self.children}\n"
        out += f"props = {self.props}"
        return out

    