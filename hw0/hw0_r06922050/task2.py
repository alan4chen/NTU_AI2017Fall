#!/usr/bin/python
# -*- coding: utf8 -*-

class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        leftSum = 0
        
        if (root.left == None) and (root.right == None):
            return 0
        
        if root.left != None:
            if (root.left.left == None) and (root.left.right == None):
                leftSum += root.left.val
            else:
                leftSum += self.sumOfLeftLeaves(root.left)
                
        if root.right != None:
            leftSum += self.sumOfLeftLeaves(root.right)
        
        return leftSum

    
if __name__ == '__main__':
    root = Node(3)
    # root.left = Node(9)
    # root.left.right = Node(3)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    sol = Solution()
    print sol.sumOfLeftLeaves(root)
    
    