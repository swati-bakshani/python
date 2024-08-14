class node:
    def __init__(self,value):
        self.value = value
        self.next = None

class linked_list:
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
    def append(self,value):
        new_node = node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        self.length -=1
        if self.length == 0:
            self.tail = None
        return temp
        # return temp.value -- ans 2pop than 1 pop than none

my_linked_list = linked_list(2)
my_linked_list.append(1)

my_linked_list.print_list()
print(my_linked_list.pop_first())
print(my_linked_list.pop_first())
print(my_linked_list.pop_first())
