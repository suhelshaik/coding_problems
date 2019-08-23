class Tree:
    def __init__(self,x):
        self.left=None
        self.data=x
        self.right=None
    def addNode(self,x):
        if self.data:
            if x<self.data:
                if self.left is None:
                    self.left=Tree(x)
                else:
                    self.left.addNode(x)
            else:
                if self.right is None:
                    self.right=Tree(x)
                else:
                    self.right.addNode(x)
        else:
            self.data=x

    def printTree(self):
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()
        print(self.data)
        




t=Tree(7)
t.addNode(4)
t.addNode(5)
t.addNode(3)
t.addNode(9)
t.addNode(8)
t.printTree()                 
