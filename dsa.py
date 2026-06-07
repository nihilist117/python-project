#practice dsa concepts
class treenode():
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
root = treenode("laptop")
hp = treenode("HP")
root.add_child(hp)
print(root.data)
print(root.children[0].data)