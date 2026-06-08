# 94. Binary Tree Inorder Traversal
"""Given the root of a binary tree, return the inorder traversal of its nodes' values.
Difficulty: Easy
Approach: Brute Force"""

def inorderTraversal(self, root) -> list[int]:
        result = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        dfs(root)
        return result