class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


# my_linked_list = LinkedList(4)
# print(my_linked_list.head.value)

    # def append(self,value):
    # def prepend(self,value):
    # def insert(self,value):

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

my_linked_list = LinkedList(4)
my_linked_list.append(3)
my_linked_list.append(6)

my_linked_list.print_list()
