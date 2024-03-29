class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self,value):
        new_node = Node(value)
        # self.top = new_node
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp

        self.height -= 1


    def print_stack(self):
        temp = self.top
        while temp is not None:

            print(temp.value)
            temp = temp.next

my_stack = Stack(4)
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.pop()
my_stack.print_stack()


