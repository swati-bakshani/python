class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

# my_linked_list = LinkedList(4)
# my_linked_list.print_list()
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None

        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp







my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.print_list()
print("printing popped values with 2 methods")
popped_value = my_linked_list.pop()
print(my_linked_list.pop().value)
print(popped_value.value)
# my_linked_list.
# print("printing length, head, tail")
# print('Lenght: ', my_linked_list.length)
# print('Head: ',my_linked_list.head.value)
# print('Tail: ',my_linked_list.tail.value)
print("Printing what left in our list")
my_linked_list.print_list()
