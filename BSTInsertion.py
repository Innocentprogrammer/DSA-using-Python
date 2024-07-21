# BST Insertion

#1. Define a class Node with instance variables left, item, and right. The variables left and right are used to refer left and right child node. The item variable is used to hold data item.

class Node:
    def __init__(self,left=None,data=None,right=None):
        self.left=left 
        self.data=data 
        self.right=right


#2. Define a class BST to implement Binary Search Tree data structure. Make __init__() method to create root instance variable to hold the reference of root node. 

class BST:
    def __init__(self,root=None):
        self.root=root


#3. In class BST, define insert method to store new data item in the binary search tree.

    def insert_item(self,data):
        new_node=Node(data)
        if self.root==None:
            self.root=new_node
        else:
            self.rinsert(self.root,new_node)
    def rinsert(self,root,new_node):
        if new_node.data < root.data:
            if root.left==None:
                root.left=new_node
            else:
                self.rinsert(root.left,new_node)
        else:
            if root.right==None:
                root.right=new_node
            else:
                self.rinsert(root.right,new_node)
   

# #4. In class BST, define a search method to find a given item in the binary search tree and return the node reference. It returns None if search failed.
    def search(self,data):
        return self.rsearch(self.root,data)
    def rsearch(self,root,data):
        if root is None or root.data==data:
            return root
        if (data < root.data):
            return self.rsearch(root.left,data)
        else:
            return self.rsearch(root.right,data)


#5. In class BST, define a method to implement inorder traversal.

    def inorder(self):
        res=[]
        self.rinorder(self.root,res)
        return res
    def rinorder(self,root,res):
        if root is not None:
            self.rinorder(root.left,res)
            res.append(root.data)
            self.rinorder(root.right,res)

    


#6. In class BST, define a method to implement preorder traversal.

    def preorder(self):
        res=[]
        self.rpreorder(self.root,res)
        return res
    def rpreorder(self,root,res):
        if root:
            res.append(root.data)
            self.rpreorder(root.left,res) 
            self.rpreorder(root.right,res)


#7. In class BST, define a method to implement postorder traversal.

    def postorder(self):
        res=[]
        self.rpostorder(self.root,res)
        return res
    def rpostorder(self,root,res):
        if root:
            self.rpostorder(root.left,res) 
            self.rpostorder(root.right,res)
            res.append(root.data)


#Driver Code:
bst=BST()
bst.insert_item(50)
bst.insert_item(30)
bst.insert_item(10)
bst.insert_item(40)
bst.insert_item(80)
bst.insert_item(70)
bst.insert_item(100)
print(bst.search(60))
print(bst.inorder())
print(bst.postorder())
print(bst.preorder())