"""
Binary Trees - Comprehensive Implementation

This module demonstrates various binary tree implementations with detailed explanations,
time/space complexity analysis, and traversal algorithms.

Binary Tree: A hierarchical data structure where each node has at most two children.
- Left child: smaller values (in BST)
- Right child: larger values (in BST)

Types covered:
1. Basic Binary Tree
2. Binary Search Tree (BST)
3. AVL Tree (Self-balancing BST)
4. Tree Traversals (Inorder, Preorder, Postorder, Level-order)

Author: Algorithm Learning Repository
"""

from collections import deque
from typing import Optional, List, Any


class TreeNode:
    """Basic tree node for binary tree implementations."""
    
    def __init__(self, data: Any):
        """
        Initialize tree node.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.data = data
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None
        self.height = 1  # For AVL tree
    
    def __str__(self):
        return str(self.data)


class BinaryTree:
    """
    Basic Binary Tree Implementation
    
    A hierarchical data structure with nodes containing data and references
    to left and right children.
    """
    
    def __init__(self):
        """
        Initialize empty binary tree.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.root: Optional[TreeNode] = None
    
    def insert_level_order(self, data: Any) -> None:
        """
        Insert node in level order (complete tree).
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        new_node = TreeNode(data)
        
        if not self.root:
            self.root = new_node
            return
        
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            
            if not node.left:
                node.left = new_node
                break
            elif not node.right:
                node.right = new_node
                break
            else:
                queue.append(node.left)
                queue.append(node.right)
    
    def inorder_traversal(self, node: Optional[TreeNode] = None, result: List[Any] = None) -> List[Any]:
        """
        Inorder traversal: Left → Root → Right
        
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height
        """
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.data)
            self.inorder_traversal(node.right, result)
        
        return result
    
    def preorder_traversal(self, node: Optional[TreeNode] = None, result: List[Any] = None) -> List[Any]:
        """
        Preorder traversal: Root → Left → Right
        
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height
        """
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node:
            result.append(node.data)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)
        
        return result
    
    def postorder_traversal(self, node: Optional[TreeNode] = None, result: List[Any] = None) -> List[Any]:
        """
        Postorder traversal: Left → Right → Root
        
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height
        """
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.data)
        
        return result
    
    def level_order_traversal(self) -> List[Any]:
        """
        Level-order traversal (BFS): Level by level from left to right
        
        Time Complexity: O(n)
        Space Complexity: O(w) where w is maximum width
        """
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            result.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def height(self, node: Optional[TreeNode] = None) -> int:
        """
        Calculate height of tree.
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if node is None:
            node = self.root
        
        if not node:
            return 0
        
        return 1 + max(self.height(node.left), self.height(node.right))
    
    def count_nodes(self, node: Optional[TreeNode] = None) -> int:
        """
        Count total number of nodes.
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if node is None:
            node = self.root
        
        if not node:
            return 0
        
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)
    
    def print_tree(self, node: Optional[TreeNode] = None, level: int = 0, prefix: str = "Root: ") -> None:
        """
        Print tree structure visually.
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if node is None:
            node = self.root
        
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.data))
            if node.left is not None or node.right is not None:
                if node.left:
                    self.print_tree(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                
                if node.right:
                    self.print_tree(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")


class BinarySearchTree(BinaryTree):
    """
    Binary Search Tree Implementation
    
    A binary tree where left subtree contains nodes with keys less than node's key,
    and right subtree contains nodes with keys greater than node's key.
    """
    
    def insert(self, data: Any) -> None:
        """
        Insert node in BST maintaining BST property.
        
        Time Complexity: O(h) where h is height
        Space Complexity: O(h) for recursion
        """
        self.root = self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node: Optional[TreeNode], data: Any) -> TreeNode:
        """Helper method for recursive insertion."""
        if not node:
            return TreeNode(data)
        
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        # Equal values not inserted (no duplicates)
        
        return node
    
    def search(self, data: Any) -> bool:
        """
        Search for value in BST.
        
        Time Complexity: O(h) where h is height
        Space Complexity: O(h) for recursion
        """
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node: Optional[TreeNode], data: Any) -> bool:
        """Helper method for recursive search."""
        if not node:
            return False
        
        if data == node.data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
    
    def delete(self, data: Any) -> None:
        """
        Delete node from BST.
        
        Time Complexity: O(h) where h is height
        Space Complexity: O(h) for recursion
        """
        self.root = self._delete_recursive(self.root, data)
    
    def _delete_recursive(self, node: Optional[TreeNode], data: Any) -> Optional[TreeNode]:
        """Helper method for recursive deletion."""
        if not node:
            return node
        
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # Node to be deleted found
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                # Node with two children: get inorder successor
                successor = self._find_min(node.right)
                node.data = successor.data
                node.right = self._delete_recursive(node.right, successor.data)
        
        return node
    
    def _find_min(self, node: TreeNode) -> TreeNode:
        """Find minimum value node in subtree."""
        while node.left:
            node = node.left
        return node
    
    def find_min(self) -> Optional[Any]:
        """
        Find minimum value in BST.
        
        Time Complexity: O(h)
        Space Complexity: O(1)
        """
        if not self.root:
            return None
        
        node = self.root
        while node.left:
            node = node.left
        return node.data
    
    def find_max(self) -> Optional[Any]:
        """
        Find maximum value in BST.
        
        Time Complexity: O(h)
        Space Complexity: O(1)
        """
        if not self.root:
            return None
        
        node = self.root
        while node.right:
            node = node.right
        return node.data
    
    def is_valid_bst(self, node: Optional[TreeNode] = None, min_val: float = float('-inf'), max_val: float = float('inf')) -> bool:
        """
        Check if tree is a valid BST.
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if node is None:
            node = self.root
        
        if not node:
            return True
        
        if node.data <= min_val or node.data >= max_val:
            return False
        
        return (self.is_valid_bst(node.left, min_val, node.data) and 
                self.is_valid_bst(node.right, node.data, max_val))


class AVLTree(BinarySearchTree):
    """
    AVL Tree Implementation (Self-balancing BST)
    
    A self-balancing binary search tree where the height difference
    between left and right subtrees is at most 1.
    """
    
    def _get_height(self, node: Optional[TreeNode]) -> int:
        """Get height of node."""
        if not node:
            return 0
        return node.height
    
    def _get_balance(self, node: Optional[TreeNode]) -> int:
        """Get balance factor of node."""
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _update_height(self, node: TreeNode) -> None:
        """Update height of node."""
        if node:
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
    
    def _rotate_right(self, y: TreeNode) -> TreeNode:
        """
        Right rotation for AVL tree balancing.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update heights
        self._update_height(y)
        self._update_height(x)
        
        return x
    
    def _rotate_left(self, x: TreeNode) -> TreeNode:
        """
        Left rotation for AVL tree balancing.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update heights
        self._update_height(x)
        self._update_height(y)
        
        return y
    
    def insert(self, data: Any) -> None:
        """
        Insert node in AVL tree maintaining balance.
        
        Time Complexity: O(log n)
        Space Complexity: O(log n)
        """
        self.root = self._insert_avl(self.root, data)
    
    def _insert_avl(self, node: Optional[TreeNode], data: Any) -> TreeNode:
        """Helper method for AVL insertion with balancing."""
        # Step 1: Perform normal BST insertion
        if not node:
            return TreeNode(data)
        
        if data < node.data:
            node.left = self._insert_avl(node.left, data)
        elif data > node.data:
            node.right = self._insert_avl(node.right, data)
        else:
            return node  # No duplicates
        
        # Step 2: Update height
        self._update_height(node)
        
        # Step 3: Get balance factor
        balance = self._get_balance(node)
        
        # Step 4: Perform rotations if needed
        # Left Left Case
        if balance > 1 and data < node.left.data:
            return self._rotate_right(node)
        
        # Right Right Case
        if balance < -1 and data > node.right.data:
            return self._rotate_left(node)
        
        # Left Right Case
        if balance > 1 and data > node.left.data:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Right Left Case
        if balance < -1 and data < node.right.data:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def delete(self, data: Any) -> None:
        """
        Delete node from AVL tree maintaining balance.
        
        Time Complexity: O(log n)
        Space Complexity: O(log n)
        """
        self.root = self._delete_avl(self.root, data)
    
    def _delete_avl(self, node: Optional[TreeNode], data: Any) -> Optional[TreeNode]:
        """Helper method for AVL deletion with balancing."""
        # Step 1: Perform normal BST deletion
        if not node:
            return node
        
        if data < node.data:
            node.left = self._delete_avl(node.left, data)
        elif data > node.data:
            node.right = self._delete_avl(node.right, data)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                successor = self._find_min(node.right)
                node.data = successor.data
                node.right = self._delete_avl(node.right, successor.data)
        
        # Step 2: Update height
        self._update_height(node)
        
        # Step 3: Get balance factor
        balance = self._get_balance(node)
        
        # Step 4: Perform rotations if needed
        # Left Left Case
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)
        
        # Left Right Case
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Right Right Case
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)
        
        # Right Left Case
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node


class TreeApplications:
    """Collection of tree-based algorithms and applications."""
    
    @staticmethod
    def lowest_common_ancestor_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Find LCA in BST.
        
        Time Complexity: O(h)
        Space Complexity: O(1)
        """
        if p.data < root.data and q.data < root.data:
            return TreeApplications.lowest_common_ancestor_bst(root.left, p, q)
        elif p.data > root.data and q.data > root.data:
            return TreeApplications.lowest_common_ancestor_bst(root.right, p, q)
        else:
            return root
    
    @staticmethod
    def is_balanced(root: Optional[TreeNode]) -> bool:
        """
        Check if binary tree is height-balanced.
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        def check_balance(node):
            if not node:
                return 0, True
            
            left_height, left_balanced = check_balance(node.left)
            right_height, right_balanced = check_balance(node.right)
            
            height = 1 + max(left_height, right_height)
            balanced = (left_balanced and right_balanced and 
                       abs(left_height - right_height) <= 1)
            
            return height, balanced
        
        _, balanced = check_balance(root)
        return balanced
    
    @staticmethod
    def diameter(root: Optional[TreeNode]) -> int:
        """
        Find diameter of binary tree.
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        def diameter_helper(node):
            if not node:
                return 0, 0  # height, diameter
            
            left_height, left_diameter = diameter_helper(node.left)
            right_height, right_diameter = diameter_helper(node.right)
            
            height = 1 + max(left_height, right_height)
            diameter = max(left_diameter, right_diameter, left_height + right_height)
            
            return height, diameter
        
        _, diameter = diameter_helper(root)
        return diameter


def demonstrate_binary_trees():
    """Demonstrate various binary tree operations."""
    print("=== Basic Binary Tree ===\n")
    
    bt = BinaryTree()
    values = [1, 2, 3, 4, 5, 6, 7]
    
    for val in values:
        bt.insert_level_order(val)
    
    print("Tree structure:")
    bt.print_tree()
    
    print(f"\nTraversals:")
    print(f"Inorder:    {bt.inorder_traversal()}")
    print(f"Preorder:   {bt.preorder_traversal()}")
    print(f"Postorder:  {bt.postorder_traversal()}")
    print(f"Level-order: {bt.level_order_traversal()}")
    
    print(f"\nTree properties:")
    print(f"Height: {bt.height()}")
    print(f"Node count: {bt.count_nodes()}")
    
    print(f"\n=== Binary Search Tree ===\n")
    
    bst = BinarySearchTree()
    bst_values = [50, 30, 70, 20, 40, 60, 80]
    
    for val in bst_values:
        bst.insert(val)
    
    print("BST structure:")
    bst.print_tree()
    
    print(f"\nBST operations:")
    print(f"Search 40: {bst.search(40)}")
    print(f"Search 45: {bst.search(45)}")
    print(f"Min value: {bst.find_min()}")
    print(f"Max value: {bst.find_max()}")
    print(f"Is valid BST: {bst.is_valid_bst()}")
    
    print(f"Inorder traversal (should be sorted): {bst.inorder_traversal()}")
    
    print(f"\nDeleting 30...")
    bst.delete(30)
    print(f"Inorder after deletion: {bst.inorder_traversal()}")
    
    print(f"\n=== AVL Tree ===\n")
    
    avl = AVLTree()
    avl_values = [10, 20, 30, 40, 50, 25]
    
    print("Inserting values in AVL tree:")
    for val in avl_values:
        print(f"Inserting {val}...")
        avl.insert(val)
    
    print("AVL tree structure:")
    avl.print_tree()
    
    print(f"AVL tree height: {avl.height()}")
    print(f"Is balanced: {TreeApplications.is_balanced(avl.root)}")


def tree_algorithm_examples():
    """Demonstrate tree algorithms."""
    print("=== Tree Algorithms ===\n")
    
    # Create a sample tree for algorithms
    bst = BinarySearchTree()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)
    
    print("Sample tree:")
    bst.print_tree()
    
    # Tree properties
    print(f"\nTree properties:")
    print(f"Diameter: {TreeApplications.diameter(bst.root)}")
    print(f"Is balanced: {TreeApplications.is_balanced(bst.root)}")
    
    # Create unbalanced tree
    unbalanced = BinarySearchTree()
    for val in [1, 2, 3, 4, 5]:
        unbalanced.insert(val)
    
    print(f"\nUnbalanced tree:")
    unbalanced.print_tree()
    print(f"Is balanced: {TreeApplications.is_balanced(unbalanced.root)}")


if __name__ == "__main__":
    print("🚀 Binary Trees - Comprehensive Tutorial\n")
    print("=" * 60)
    
    # Demonstrate all tree types
    demonstrate_binary_trees()
    
    # Show tree algorithms
    print("\n" + "=" * 60)
    tree_algorithm_examples()
    
    print("\n" + "=" * 60)
    print("✅ Binary trees tutorial completed!")
    print("\n📝 Key Takeaways:")
    print("• Binary trees: hierarchical structure with at most 2 children")
    print("• BST: maintains sorted order, O(h) operations")
    print("• AVL: self-balancing BST, guarantees O(log n) operations")
    print("• Traversals: inorder (sorted for BST), preorder, postorder, level-order")
    print("• Tree algorithms: balance checking, diameter, LCA")
    print("• Choose tree type based on use case and balance requirements")