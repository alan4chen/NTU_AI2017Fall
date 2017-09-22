from hw0_r06922048.task2 import *

###

import random

class Question(object):

    def setTree(self, d, isLeft):
        sum = 0
        node = Node(0)
        if d == 0:
            sum = random.randint(100, 500)
            node = Node(sum)
            if isLeft:
                return node, sum
            else:
                return node, 0
        if random.random() > 0.3:
            left_node, left_val = self.setTree(d - 1, True)
            node.left = left_node
            sum += left_val
        if random.random() > 0.3:
            right_node, right_val = self.setTree(d - 1, False)
            node.right = right_node
            sum += right_val
        if node.right == None and node.left == None:
            sum = random.randint(100, 500)
            node = Node(sum)
            if isLeft:
                return node, sum
            else:
                return node, 0
        return node, sum


if __name__ == "__main__":

    # Simple Test
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    sol = Solution()
    print sol.sumOfLeftLeaves(root)

    # Test1
    random.seed(1)

    root, s = Question().setTree(20, True)
    print sol.sumOfLeftLeaves(root), s
    assert sol.sumOfLeftLeaves(root) == s