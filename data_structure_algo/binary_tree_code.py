# constructor creation

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
# Insert node
    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    # def insert(self,value):
    #     new_node = Node(value)
    #     if self.root is None:
    #         self.root = new_node
    #         return True
    #     temp = self.root
    #     while(True):
    #         if new_node.value == temp.value:
    #             return False
    #         if new_node.value < temp.value:
    #             if temp.left is None:
    #                 temp.left = new_node
    #                 return True
    #             temp = temp.left
    #         else:
    #             if temp.right is None:
    #                 temp.right = new_node
    #                 return True
    #             temp = temp.right





my_binarytree = BinarySearchTree()
print(my_binarytree.root)
my_binarytree.insert(2)
my_binarytree.insert(1)
my_binarytree.insert(3)

print(my_binarytree.root.value)
print(my_binarytree.root.left.value)
print(my_binarytree.root.right.value)


