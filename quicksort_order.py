class Stack:
    MAX_SIZE = 100
    
    def __init__(self):
        self.arr = [0] * self.MAX_SIZE
        self.top = -1
    
    def push_to_stack(self, value: int):
        if self.top < self.MAX_SIZE - 1:
            self.top += 1
            self.arr[self.top] = value
        else:
            print("Stack Overflow")
    
    def pop_from_stack(self) -> int:
        if self.top >= 0:
            value = self.arr[self.top]
            self.top -= 1
            return value
        print("Stack Underflow")
        return -1

    def is_empty(self) -> bool:
        return self.top == -1


class Queue:
    MAX_SIZE = 100
    
    def __init__(self):
        self.arr = [0] * self.MAX_SIZE
        self.front = -1
        self.rear = -1
    
    def enqueue_to_queue(self, value: int):
        if self.rear < self.MAX_SIZE - 1:
            self.rear += 1
            self.arr[self.rear] = value
        else:
            print("Queue Overflow")
    
    def dequeue_from_queue(self) -> int:
        if self.front < self.rear:
            self.front += 1
            return self.arr[self.front]
        print("Queue Underflow")
        return -1
    
    def is_empty(self) -> bool:
        return self.front == self.rear


class SinglyLinkedList:
    class Node:
        def __init__(self, data, next_index=-1):
            self.data = data
            self.next = next_index
    
    MAX_SIZE = 100
    
    def __init__(self):
        self.nodes = [None] * self.MAX_SIZE
        self.head = -1
        self.free_index = 0
    
    def insert_into_linked_list(self, value: int):
        if self.free_index < self.MAX_SIZE:
            self.nodes[self.free_index] = self.Node(value, self.head)
            self.head = self.free_index
            self.free_index += 1
        else:
            print("List Full")
    
    def display_linked_list(self):
        temp = self.head
        while temp != -1:
            print(self.nodes[temp].data, end=" -> ")
            temp = self.nodes[temp].next
        print("NULL")

if __name__ == "__main__":
    stack = Stack()
    stack.push_to_stack(10)
    stack.push_to_stack(20)
    print("Popped from stack:", stack.pop_from_stack())
    
    queue = Queue()
    queue.enqueue_to_queue(30)
    queue.enqueue_to_queue(40)
    print("Dequeued from queue:", queue.dequeue_from_queue())
    
    linked_list = SinglyLinkedList()
    linked_list.insert_into_linked_list(50)
    linked_list.insert_into_linked_list(60)
    linked_list.display_linked_list()
