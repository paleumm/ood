class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.num = 0

    def insert(self, cur: Node, data: int):
        if self.root is None:
            print("*")
            self.root = Node(data)
            return self.root
        
        # if cur.data == data:
        #     return self.root
        
        if cur.data <= data:
            if cur.right is not None:
                print("R",end="")
                self.insert(cur.right, data)
            else:
                print("R*")
                cur.right = Node(data)
        else:
            if cur.left is not None:
                print("L",end="")
                self.insert(cur.left, data)
            else:
                print("L*")
                cur.left = Node(data)
        return self.root

    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
root = T.root
for i in inp:
    root = T.insert(root, i)

# T.printTree(root)