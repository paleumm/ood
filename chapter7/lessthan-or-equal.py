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

    def findLoEQ(self, root, k, count):
        if root is None:
            return 0

        if root.data <= k:
            count += 1
        
        count += self.findLoEQ(root.left,k,0)
        count += self.findLoEQ(root.right,k,0)
        return count

T = BST()
ii = input('Enter Input : ').split("/")
inp = [int(i) for i in ii[0].split()]
root = T.root
for i in inp:
    root = T.insert(root, i)
T.printTree(root)
print(f'--------------------------------------------------')
print(T.findLoEQ(T.root, int(ii[1]),0))