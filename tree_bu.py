class Node:
    def __init__(self, value):
        self._value= value
        self._parent= None
        self._children= []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, node):
        if node not in self.children:
            self.children.append(node)
            node.parent=self

    def remove_child(self, node):
        if node in self.children:
            self.children.remove(node)
            node.parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        if self.parent:
            self.parent.remove_child(self)
        if value is not None:
            value.add_child(self)

node1 = Node("root1")
node2 = Node("root2")
node3 = Node("root3")

node3.parent = node1
node3.parent = node2

print(node1.children)
print(node2.children)
