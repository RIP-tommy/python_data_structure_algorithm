class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class Binary_Tree:
    def __init__(self):
        self.root = None
        self.current = None
        self.left = None
        self.right = None
    
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            self.current = self.root
        else:
            while True:
                if self.current.data is data:
                    break
                if data < self.current.data and not self.left:
                    self.left = Node(data)
                elif data < self.current.data and self.left:
                    self.current = self.left
                elif data > self.current.data and not self.right:
                    self.right = Node(data)
                elif data > self.current.data and self.right:
                    self.current = self.right

    def in_order(self):
        if self.left:
            self.current = self.left
        else:
            print(self.current.data)

node = (50, 15, 62, 5, 20, 58, 91, 3, 8, 37, 60, 24)

tree = Binary_Tree()

for i in node:
    tree.insert(i)
