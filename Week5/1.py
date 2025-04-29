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
    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.pointer = self.head
        self.head = new_node
    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.pointer:
            temp = temp.pointer
        temp.pointer = new_node

    def insert_at_middle(self, prev_node, new_data):
        if not prev_node:
            print("Previous node must be in the LinkedList.")
            return
        new_node = Node(new_data)
        new_node.pointer = prev_node.pointer
        prev_node.pointer = new_node

    def remove_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.pointer
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.pointer
        if not temp:
            return
        prev.pointer = temp.pointer
        temp = None

# Inisialisasi linked list
llist = LinkedList()
llist.insert_at_end(3)
llist.insert_at_end(5)
llist.insert_at_end(2)
llist.insert_at_end(6)
llist.insert_at_end(9) 
llist.insert_at_end(7)

print("Linked List awal:")
llist.traverse()

# Insert di awal
llist.insert_at_beginning(1)
print("Setelah insert di awal:")
llist.traverse()

# Insert di akhir
llist.insert_at_end(10)
print("Setelah insert di akhir:")
llist.traverse()

# Insert di tengah setelah node dengan nilai 5
temp = llist.head
while temp and temp.data != 5:
    temp = temp.pointer
llist.insert_at_middle(temp, 4)
print("Setelah insert di tengah:")
llist.traverse()

# Hapus node dengan nilai 6
llist.remove_node(6)
print("Setelah menghapus node 6:")
llist.traverse()

print("##########################################################")
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
