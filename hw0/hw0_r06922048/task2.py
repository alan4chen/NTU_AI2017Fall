"""
    Created by Po-Yao Chen
    2017.9.11
"""


class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def traverseSum(self, node, isLeft):
        sum = 0
        if isLeft and node.left == None and node.right == None:
            return node.val
        if node.left != None:
            sum += self.traverseSum(node.left, True)
        if node.right != None:
            sum += self.traverseSum(node.right, False)
        return sum

    def sumOfLeftLeaves(self, root):
        return self.traverseSum(root, True)




