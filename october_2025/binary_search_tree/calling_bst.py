class BSTNode:
    def __init__(self, val = None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        """
        - If self.val not specified, create root Node
        - If you insert same number as root -> return nothing
        """
        if not self.val:
            self.val = val
            return
        
        if self.val == val:
            return

        """
        - Check if left or right child exists, if so call insert() method again (recursively)
        - otherwise, put another BSTNode to left or right
        """
        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return
        
        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)


    """
    - Helper function
    - We know ROOT node and we also know that lowest value will be on the lowest side
    - Iterate till you find leaf NODE which have None value on left
    """
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    """
    - Same as with minimum, but we looking for most right Node
    """
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val


    """
    - Recursive function, return new state after delete operation
    - It helps parent whose hcild has been deleted to properly set it's left or right data member to 'None'
    """
    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            self.left = self.left.delete(val)
            return self
        if val > self.val:
            self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self


    """
    - Return TRUE / FALSE depending on whether a give value exists in the tree 
    """
    def exists(self, val):
        if val == self.val:
            return True
        
        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)
        
        if self.right == None:
            return False
        return self.right.exists(val)


    """
    - Print tree in readable format 
    """
    """
    - First check the left node, then middle node, then right node
    """
    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals

def main():
    nums = [20, 10, 30, 2, 15, 25, 35]
    bst = BSTNode()
    for num in nums:
        bst.insert(num)

    print("preorder:")
    print(bst.preorder([]))

    #print("postorder:")
    #print(bst.postorder([]))
    #print("#")

    print("inorder:")
    print(bst.inorder([]))



main()