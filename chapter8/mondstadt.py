class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 


class Tree:

    def __init__(self):
        self.root = None
        self.num = 0


    def insert(self, val):  
        if self.root == None:
            self.root = Node(val)
            self.num += 1

        else:
            h = height(self.root)
            max_node = pow(2,h+1)-1
            current = self.root

            if self.num+1 > max_node:
                while(current.left != None):
                    current = current.left
                current.left = Node(val)
                self.num+=1

            elif self.num+1 == max_node:
                while(current.right != None):
                    current = current.right
                current.right = Node(val)
                self.num+=1
            else:
                if self.num+1 <= max_node-((max_node-(pow(2,h)-1))/2):
                    insert_subtree(current.left,self.num - round(pow(2,h)/2),val)
                else:
                    insert_subtree(current.right,self.num - pow(2,h),val)
                self.num+=1

    def inorder(self, node: Node, s: int) -> int:
        if node is None:
            return 0
        
        q = self.inorder(node.left, 0)
        q += node.data
        q += self.inorder(node.right, 0)

        return q

    def findPower(self, idx1, idx2):
        k1 = T.inorder(T.bfs(idx1),0)
        k2 = T.inorder(T.bfs(idx2),0)

        if k1 > k2:
            print(f'{idx1}>{idx2}')
        elif k1 < k2:
            print(f'{idx1}<{idx2}')
        else:
            print(f'{idx1}={idx2}')

        

    def bfs(self, idx) -> Node:
        l = []
        l.append(self.root)
        count = -1

        while len(l) > 0:
            n = l.pop(0)
            count += 1
            if count == idx:
                return n
            if n.left is not None:
                l.append(n.left)
            if n.right is not None:
                l.append(n.right)
                    

def insert_subtree(r,num,val):
    if r != None:
        h = height(r)
        max_node = pow(2,h+1) - 1
        current = r

        if num+1 > max_node:
            while(current.left != None):
                current = current.left
            current.left = Node(val)
            return

        elif num+1 == max_node:
            while(current.right != None):
                current = current.right
            current.right = Node(val)
            return
        if num+1 <= max_node-((max_node-(pow(2,h)-1))/2):
            insert_subtree(current.left,num - round(pow(2,h)/2),val)
        else:
            insert_subtree(current.right,num - pow(2,h),val)
    else:
        return

def height(root) -> int:
    if root == None:
        return -1
    else:
        left = height(root.left)
        right = height(root.right)
        if left>right:
            return left + 1
        else:
            return right + 1

                       

def printTree90(node, level = 0):
    if node != None:

        printTree90(node.right, level + 1)

        print('     ' * level, node)

        printTree90(node.left, level + 1)

T = Tree()
inp = input('Enter Input : ').split("/")
p = [int(i) for i in inp[0].split()]
pair = [i for i in inp[1].split(",")]

print(sum(p))

for i in p:
    T.insert(i)

for pp in pair:
    K = pp.split()
    T.findPower(int(K[0]),int(K[1]))
