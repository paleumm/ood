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
            self.root = Node(data)
            self.num += 1
            return self.root
        
        if cur.data == data:
            return self.root
        
        if cur.data < data:
            if cur.right is not None:
                self.insert(cur.right, data)
            else:
                cur.right = Node(data)
                self.num += 1
        else:
            if cur.left is not None:
                self.insert(cur.left, data)
            else:
                cur.left = Node(data)
                self.num += 1
        
        return self.root

    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def getHeight(self, root):
        if root is None:
            return 0

        l = self.getHeight(root.left)
        r = self.getHeight(root.right)

        if l > r:
            return l + 1
        else:
            return r + 1



T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
root = T.root
for i in inp:
    root = T.insert(root, i)
print(f'Height of this tree is : {T.getHeight(T.root)-1}')