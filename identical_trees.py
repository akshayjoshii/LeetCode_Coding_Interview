# Recursive Approach to identify if 2 trees M & N are identical or not (both data and structure of the tree)
# Complexity: O(MxN) 

class node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class identical:
    def isIdentical(self, tree_1, tree_2):
        # If one of the tree is blank
        if tree_1 is None or tree_2 is None:
            return False
            
        # Both the trees are blank
        if tree_1 is None and tree_2 is None:
            return True
        
        # Recuresive call until the depth of the tree is reached
        if (tree_1 and tree_2) is not None:
            return ((tree_1.data == tree_2.data) and
                    self.isIdentical(tree_1.left, tree_2.left) and
                    self.isIdentical(tree_1.right, tree_2.right))
        

if __name__ == '__main__':
    # Populate both the trees
    tree_1 = node(10)
    tree_1.right = node(15)
    tree_1.left = node(5)
    tree_1.left.left = node(3)
    tree_1.right.right = node(18)

    tree_2 = node(10)
    tree_2.right = node(15)
    tree_2.left = node(5)
    # tree_2.left.left = node(3)
    # tree_2.right.right = node(18)

    result = identical().isIdentical(tree_1, tree_2)
    if result:
       print("Both the trees are identical") 
    
    else:
        print("Both the trees are NOT identical")


# Iterative method to do the same