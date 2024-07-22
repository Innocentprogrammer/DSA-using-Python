# BST Insertion

#1. Define a class Node with instance variables left, item, and right. The variables left and right are used to refer left and right child node. The item variable is used to hold data item.

class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data 
        self.left=left 
        self.right=right


#2. Define a class BST to implement Binary Search Tree data structure. Make __init__() method to create root instance variable to hold the reference of root node. 

class BST:
    def __init__(self):
        self.root=None


#3. In class BST, define insert method to store new data item in the binary search tree.

    def insert_item(self,data):
        self.root=self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left=self.rinsert(root.left,data)
        elif data > root.data:
            root.right=self.rinsert(root.right,data)
        return root
    

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


# BST Deletion

# Q1. In class BST, define a method to find minimum value item node.

    def minValue(self,root):
        current=root 
        while current.left is not None:
            current=current.left
        return current.data


# Q2. In class BST, define a method to find maximum value item node.

    def maxValue(self,root):
        current=root 
        while current.right is not None:
            current=current.right
        return current.data
        

# Q3. In class BST, define a method to delete a node from binary search tree. 

    def delete(self,data):
        self.root= self.deleteNode(self.root,data)
    def deleteNode(self,root,data):
        if root is None:
            return root
        if data < root.data:
            root.left=self.deleteNode(root.left,data)
        elif data > root.data:
            root.right=self.deleteNode(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                root.data = self.minValue(root.right)
                root.right = self.deleteNode(root.right,root.data)
            return root
            


# Q4. In class BST, define a method size to return the number of elements present in the BST. 

    def size(self):
        if self.root is not None:
            res = self.inorder()
            return len(res)
        else:
            return 0


#Driver Code:
bst=BST()
#insertion 
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
print(bst.size())
#deletion
bst.delete(50)
print(bst.inorder())
print(bst.size())