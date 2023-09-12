class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _fix_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        self._fix_height(x)
        self._fix_height(y)
        return y

    def _rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        self._fix_height(y)
        self._fix_height(x)
        return x

    def _balance(self, node):
        self._fix_height(node)
        balance = self._balance_factor(node)

        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def insert(self, root, key):
        if root is None:
            return Node(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        return self._balance(root)

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            min_node = self._find_min(root.right)
            root.key = min_node.key
            root.right = self.delete(root.right, min_node.key)

        return self._balance(root)

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=" ")
            self.inorder_traversal(root.right)

# Exemplo de uso
avl_tree = AVLTree()
root = None

root = avl_tree.insert(root, 10)
root = avl_tree.insert(root, 20)
root = avl_tree.insert(root, 30)

avl_tree.inorder_traversal(root)  # Deve imprimir "10 20 30"
