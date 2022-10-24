from re import I


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

    def insert(self, cur: Node, data: int):
        if self.root is None:
            self.root = Node(data)
            return self.root
        
        if cur.data == data:
            return self.root
        
        if cur.data < data:
            if cur.right is not None:
                self.insert(cur.right, data)
            else:
                cur.right = Node(data)
        else:
            if cur.left is not None:
                self.insert(cur.left, data)
            else:
                cur.left = Node(data)
        
        return self.root

    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def sumTree(self, root):
        if root is None:
            return 0
        
        suml = self.sumTree(root.left)
        sumr = self.sumTree(root.right)

        return root.data + suml + sumr
    
T = BST()
inp = input('Enter Input : ').split('/')
nd = [int(i) for i in inp[1].split()]
n = int(inp[0])

if len(nd) != (n//2 + 1) or n % 2 == 0:
    print('Incorrect Input')
    exit(0)

treeLs = []

lev = 0
i = 1
while True:
    if len(nd) < pow(2,i):
        lev = i
        break
    i += 1

for ndd in nd:
    ndd = Node(ndd)
    treeLs.append(ndd)

# for i in range(len(nd)/2):
#     t1 = treeLs.pop(0)
#     t2 = treeLs.pop(0)
#     mi = min(t1.data, t2.data)
#     newnode = Node(mi)
#     t1.data -= mi
#     t2.data -= mi
#     newnode.left = t1
#     newnode.right = t2
diff = pow(2,lev) - pow(2,lev-1)
nx = diff - len(nd)

while len(treeLs) > 1:
    t1 = treeLs.pop(0)
    t2 = treeLs.pop(0)
    mi = min(t1.data, t2.data)
    newnode = Node(mi)
    t1.data -= mi
    t2.data -= mi
    newnode.left = t1
    newnode.right = t2

    if len(treeLs) <= nx:
        treeLs.insert(0, newnode)
    else:
        if len(treeLs) % 2 == 0 and len(treeLs) > 1:
            treeLs.append(newnode)
        else:
            treeLs.insert(0, newnode)

T.printTree(treeLs[0])
print(T.sumTree(treeLs[0]))

