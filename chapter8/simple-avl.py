class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        return str(self.data)

class AVL:

    def __init__(self) -> None:
        self.root = None

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def insert(self, root, data):
        if root is None:
            return Node(data)
        elif root.data > data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        bFactor = self.getBalance(root)

        if bFactor > 1:
            if self.getBalance(root.left) < 0:
                root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if bFactor < -1:
            if self.getBalance(root.right) > 0:
                root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root
        

    def getHeight(self, root):
        if root is None:
            return 0
        return root.height

    def getBalance(self, root):
        if root is None:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

T = AVL()
inp = [int(i) for i in input('Enter Input : ').split()]
root = T.root
for i in inp:
    print(f'Insert : ( {i} )')
    root = T.insert(root, i)
    T.printTree(root)
    print('--------------------------------------------------')