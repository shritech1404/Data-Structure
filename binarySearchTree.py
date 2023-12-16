class binarySearchTree:
    # initialize property of the tree
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    # check tree is empty or not if it is empty then add new node as root node else go for next condition
    # check if new node == root node then ignore it (tree does not allow duplicate values)
    # check if new node < root node then go in to left sub tree else
    # check if new node > root node then go in to right sub tree
    # do this recursively until new node insert at correct position
    def insert(self, data):
        if self.key is None:
            self.key = data
            return 
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = binarySearchTree(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else: 
                self.rchild = binarySearchTree(data)

    # check tree is empty or not if it is not empty
    # check if x == root then node found else go for next condition
    # check if x < root then search in left sub tree else go for next condition
    # check if x > root then search in right sub tree
    # do this recursively until you find x
    def search(self, x):
        if self.key == x:
            print("Node Found!")
            return
        if x < self.key:
            if self.lchild:
                self.lchild.search(x)
            else:
                print("Node is Not Found!")
        else:
            if self.rchild:
                self.rchild.search(x)
            else:
                print('Node is Not Found!')

    # root node, left node, right node
    def preOrder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preOrder()
        if self.rchild:
            self.rchild.preOrder()

    # left node, root node, right node
    def inOrder(self):
        if self.lchild:
            self.lchild.inOrder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inOrder()

    # left node, right node, root node
    def postOrder(self):
        if self.lchild:
            self.lchild.postOrder()
        if self.rchild:
            self.rchild.postOrder()
        print(self.key, end=" ")

    # check tree is empty or not if it is not empty
    # find the node which we want to delete
    # delete node:
        # if that node contain 0 child then delete directly
        # if that node contain 1 child then replace that node with it's child
        # if that node contain 2 childs then:
            # replace that node with left child or
            # replace that node with right child
    def delete(self, x):
        if self.key is None:
            print("Tree is empty!")
            return
        if x < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(x)
            else:
                print('Given node is not present in the tree!')
        elif x > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(x)
            else:
                print('Given node is not present in the tree!')
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self
        

BST = binarySearchTree(60)
lst = [10,20,30,40,50,70,80,90,100]
for i in lst:
    BST.insert(i)
print('Search')
BST.search(10)
print('Pre-order')
BST.preOrder()
print()
print('In-orders')
BST.inOrder()
print()
print('Post-orders')
BST.postOrder()
print()
print('Delete 50')
BST.delete(50)
print('Post-orders')
BST.postOrder()
print()
