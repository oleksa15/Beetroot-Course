# coding = UTF-8

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, data):

        if self.head is None:
            self.head = Node(data)

        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):

        if self.is_empty():
            return None

        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data

    def peek(self):

        if self.is_empty():
            return None

        else:
            return self.head.data

    def display(self):

        iter_node = self.head
        if self.is_empty():
            print("Stack Underflow")

        else:

            while iter_node is not None:
                print(iter_node.data, "->", end=" ")
                iter_node = iter_node.next
            return

    def __repr__(self):
        representation = "<Stack: "
        current = self.head
        while current is not None:
            representation += f"{current.data} "
            current = current.next
        return representation +">"

    def __str__(self):
        return self.__repr__()

my_stack = Stack()

my_stack.push(11)
my_stack.push(22)
my_stack.push(33)
my_stack.push(44)

print(my_stack)
my_stack.display()

print("\nTop element is ", my_stack.peek())

my_stack.pop()
my_stack.pop()

my_stack.display()

print("\nTop element is ", my_stack.peek())