class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class BST:
    def create(self,data):
        return Node(data)
    def insert(self,node,data):
        if node is None:
            return self.create(data)
        if data < node.data:
            node.left=self.insert(node.left,data)
        elif data > node.data:
            node.right=self.insert(node.right,data)
        return node
    def Inorder(self,node):
        if node is not None:
            self.Inorder(node.left)
            print(node.data,end="->")
            self.Inorder(node.right)

tree=BST()
root=tree.create(8)
a=int(input("Enter a no of nodes needed: "))
for i in range(a):
    tree.insert(root,int(input()))
print("Inorder traversal of BST: ")
tree.Inorder(root)
