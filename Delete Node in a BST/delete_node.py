# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bst_to_tree(bst):
    """turns bst list into a tree"""
    if not bst or bst[0] is None:
        return None

    root = TreeNode(bst[0])
    tree_queue = deque([root])
    num = 1

    while tree_queue and num < len(bst):
        node = tree_queue.popleft()
        if num < len(bst) and bst[num] is not None:
            node.left = TreeNode(bst[num])
            tree_queue.append(node.left)
        num += 1

        if num < len(bst) and bst[num] is not None:
            node.right = TreeNode(bst[num])
            tree_queue.append(node.right)
        num += 1

    return root


class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            min_node = self.find_minimal(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)

        return root

    def find_minimal(self, node):
        while node.left:
            node = node.left
        return node
