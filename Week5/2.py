class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.pointer
        print("None")

    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.pointer:
            temp = temp.pointer
        temp.pointer = new_node

    def sum_linked_list(self):
        temp = self.head
        total = 0
        while temp:
            total += temp.data
            temp = temp.pointer
        return total

# Inisialisasi linked list
llist = LinkedList()
llist.insert_at_end(3)
llist.insert_at_end(5)
llist.insert_at_end(2)
llist.insert_at_end(6)
llist.insert_at_end(9)
llist.insert_at_end(7)

print("Linked List:")
llist.traverse()

# Menjumlahkan nilai dalam linked list
total_sum = llist.sum_linked_list()
print("Total sum of linked list:", total_sum)
