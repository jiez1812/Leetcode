class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        from pprint import pformat

        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({f"{self.value}":(self.left, self.right)}, indent=1)

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root
    
    def is_empty(self):
        return self.root == None

    def __str__(self) -> str:
        return str(self.root)
    
    def __insert(self, value):
        """
        Insert a new node in Binary Search Tree with value label
        """
        new_node = Node(value)
        if self.is_empty():
            self.root = new_node
        else:
            parent_node = self.root # from root
            if parent_node is None:
                return None
            while True: # While we don't get to a leaf
                if value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node = parent_node.left
                else:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
            new_node.parent = parent_node

    def __reassign_nodes(self, node: Node, new_children: Node):
        if new_children is not None: # reset children
            new_children.parent = node.parent
        if node.parent is not None: # reset its parent
            if self.is_right(node): # If it is the right childrent
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = None
    
    def is_right(self, node:Node):
        if node.parent and node.parent.right:
            return node == node.parent.right
        return False

    def insert(self, *values):
        for value in values:
            self.__insert(value)

    def search(self, value):
        if self.is_empty():
            raise IndexError("Warning: Tree is empty! please use another.")
        else:
            node = self.root
            while node is not None and node.value is not value:
                node = node.left if value < node.value else node.right
            return node

    def get_max(self, node:Node=None):
        if node is None:
            node = self.root
        if self.root is None:
            return None
        if not self.is_empty():
            while node.right is not None:
                node = node.right
        return node

    def get_min(self, node:Node=None):
        if node is None:
            node = self.root
        if self.root is None:
            return None
        if not self.is_empty():
            node = self.root
            while node.left is not None:
                node = node.left
        return node

    def remove(self, value):
        node = self.search(value)
        if node is not None:
            if node.left is None and node.right is None:
                self.__reassign_nodes(node, None)
            elif node.left is None:
                self.__reassign_nodes(node, node.right)
            elif node.right is None:
                self.__reassign_nodes(node, node.left)
            else:
                tmp_node = self.get_max(node.left)
                self.remove(tmp_node.value)
                node.value = (tmp_node.value)

    def preorder_traverse(self, node:Node=None):
        if node:
            print(node.value)
            self.preorder_traverse(node.left)
            self.preorder_traverse(node.right)

    def inorder_traverse(self, node:Node=None):
        if node:
            self.inorder_traverse(node.left)
            print(node.value)
            self.inorder_traverse(node.right)

    def postorder_traverse(self, node:Node=None):
        if node:
            self.postorder_traverse(node.left)
            self.postorder_traverse(node.right)
            print(node.value)

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(8, 3, 6, 1, 10, 14, 13, 4, 7, 11)
    bst.preorder_traverse(bst.root)
    print('='*5)
    bst.inorder_traverse(bst.root)
    print('='*5)
    bst.postorder_traverse(bst.root)