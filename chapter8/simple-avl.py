class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class AVL:

    def __init__(self) -> None:
        pass

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def insert(self, data):
        pass

    def getHeight(self, root):
        if root is None:
            return 0

        l = self.getHeight(root.left)
        r = self.getHeight(root.right)

        if l > r:
            return l + 1
        else:
            return r + 1