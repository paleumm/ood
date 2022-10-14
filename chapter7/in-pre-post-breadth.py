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
    
    def preorder(self, node: Node, q: list) -> list:
        if node is None:
            return []
        
        q.append(str(node.data))
        q += self.preorder(node.left, [])
        q += self.preorder(node.right, [])

        return q

    def inorder(self, node: Node, q: list) -> list:
        if node is None:
            return []
        
        q = self.inorder(node.left, [])
        q.append(str(node.data))
        q += self.inorder(node.right, [])

        return q

    def postorder(self, node: Node, q: list) -> list:
        if node is None:
            return []
        
        q = self.postorder(node.left, [])
        q += self.postorder(node.right, [])
        q.append(str(node.data))

        return q

    def breadthFirst(self) -> list:
        if self.root is None:
            return []
        
        q = [self.root]
        out = []
        
        while len(q) != 0:
            cur = q.pop(0)

            out.append(str(cur.data))
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
        
        return out

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
root = T.root
for i in inp:
    root = T.insert(root, i)

print(f'Preorder : {" ".join(T.preorder(T.root, []))}')
print(f'Inorder : {" ".join(T.inorder(T.root, []))}')
print(f'Postorder : {" ".join(T.postorder(T.root, []))}')
print(f'Breadth : {" ".join(T.breadthFirst())}')



