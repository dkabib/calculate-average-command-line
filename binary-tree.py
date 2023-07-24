# Binary Tree testing

class Node:
    def __init__(self, key):
        # Node has a value (key), left child, and right child
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        # Initialize an empty binary tree with the root node set to None
        self.root = None

    def insert(self, key):
        # Insert a new node with the given key into the binary tree
        if self.root is None:
            # If the tree is empty, create the root node
            self.root = Node(key)
        else:
            # If the tree is not empty, call the private insert function
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, current_node, key):
        # Insert a new node recursively
        if key < current_node.key:
            # If the key is less than the current node's key, go left
            if current_node.left is None:
                # If there is no left child, create a new node and set it as the left child
                current_node.left = Node(key)
            else:
                # If there is a left child, recursively call the function with the left child
                self._insert_recursively(current_node.left, key)
        else:
            # If the key is greater than or equal to the current node's key, go right
            if current_node.right is None:
                # If there is no right child, create a new node and set it as the right child
                current_node.right = Node(key)
            else:
                # If there is a right child, recursively call the function with the right child
                self._insert_recursively(current_node.right, key)

    def search(self, key):
        # Search for a key in the binary tree and return True if found, otherwise return False
        return self._search_recursively(self.root, key)

    def _search_recursively(self, current_node, key):
        # Helper function to search for a key recursively
        if current_node is None:
            # If the current node is None (reached a leaf node), the key is not in the tree
            return False

        if current_node.key == key:
            # If the current node's key matches the search key, return True
            return True
        elif key < current_node.key:
            # If the search key is less than the current node's key, go left
            return self._search_recursively(current_node.left, key)
        else:
            # If the search key is greater than the current node's key, go right
            return self._search_recursively(current_node.right, key)

    def inorder_traversal(self):
        # Perform an inorder traversal of the binary tree and return the elements as a list
        result = []
        self._inorder_traversal_recursively(self.root, result)
        return result

    def _inorder_traversal_recursively(self, current_node, result):
        # Helper function for inorder traversal
        if current_node is not None:
            # Traverse left subtree
            self._inorder_traversal_recursively(current_node.left, result)
            # Visit the current node and add its key to the result list
            result.append(current_node.key)
            # Traverse right subtree
            self._inorder_traversal_recursively(current_node.right, result)


# Test the Binary Tree
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(59)
    tree.insert(30)
    tree.insert(71)
    tree.insert(18)
    tree.insert(40)
    tree.insert(60)
    tree.insert(87)

    print("Inorder Traversal:", tree.inorder_traversal())

    search_key = 60
    if tree.search(search_key):
        print(f"{search_key} is found in the tree.")
    else:
        print(f"{search_key} is not found in the tree.")
    
    search_key = 45
    if tree.search(search_key):
        print(f"{search_key} is found in the tree.")
    else:
        print(f"{search_key} is not found in the tree.")
