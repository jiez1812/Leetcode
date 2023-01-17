class Node:
    def __init__(self, value=None):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
        else:
            parent = self.root
            while True:
                if node.value < parent.value:
                    if parent.left is None:
                        parent.left = node
                        break
                    else:
                        parent = parent.left
                else:
                    if parent.right is None:
                        parent.right = node
                        break
                    else:
                        parent = parent.right
            node.parent = parent

    def search(self, value):
        current = self.root
        while True:
            if current == None:
                return None

            if current.left == None and current.right == None:
                return None

            if value == current.value:
                return current
            elif value != current.value and value < current.value:
                current = current.left
            elif value != current.value and value > current.value:
                current = current.right

    def remove(self, value):
        node = self.search(value)
        if node:
            pass
        else:
            return None

    def inorder_tranverse(self, node:Node, nums:list=[]):
        if node != None:
            self.inorder_tranverse(node.left, nums)
            nums.append(node.value)
            self.inorder_tranverse(node.right, nums)
        return nums
    
if __name__ == '__main__':
    import random
    bst = BinarySearchTree()
    num_list = random.sample(range(50), 10)
    print(num_list)
    for i in num_list:
        bst.insert(i)
    print(bst.inorder_tranverse(bst.root))
    bst.search(num_list[3])