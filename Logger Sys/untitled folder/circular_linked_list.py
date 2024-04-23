#Code by Nallapati Bala Yashaswini
class CircularLinkedList:
    def __init__(self, capacity=10):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.size = 0

    def add(self, data):
        new_node = LogNode(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node  # Circular link
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        
        if self.size == self.capacity:
            self.head = self.head.next  # Remove the oldest log, i.e., move head pointer
        else:
            self.size += 1

    def display(self):
        if self.size == 0:
            print("No logs to display.")
            return
        
        current = self.head
        for _ in range(self.size):
            print(current.data)
            current = current.next
