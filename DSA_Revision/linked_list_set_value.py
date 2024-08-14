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
        self.length += 1
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    def set_value(self,index,value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False


my_linked_list = linked_list(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

my_linked_list.print_list()
print("------- after change 4 is updated-------")
my_linked_list.set_value(1,4)
my_linked_list.print_list()




