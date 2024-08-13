class node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Linked_list:
    def __init__(self,value):
        new_node = node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_linked_list = Linked_list(4)
my_linked_list = Linked_list(6)
my_linked_list.print_list()



