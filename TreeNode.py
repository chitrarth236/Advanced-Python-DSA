class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self):
        self.root = None
    
    def takeInput(self):
        data = input("Enter data: ")
        root = TreeNode(data)
        nChildren = int(input("Enter the No. of Childrens of {}: ".format(root.data)))
        for i in range(nChildren):
            node = self.takeInput()
            root.children.append(node)

        return root

    def printTree(self,root):
        print(root.data,": ",end="")
        for i in root.children:
            print(i.data," ",end=",")
        for i in root.children:
            self.printTree(i)

if __name__ == "__main__":
    t = Tree()
    t_root = t.takeInput()
    t.printTree(t_root)