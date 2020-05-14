
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubLinkedList:

    def __init__(self):
        self.head = None


# reverse iteration


    def reverse(self):
        temp = None
        current = self.head

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:
            self.head = temp.prev

    def push(self, new_data):

        new_node = Node(new_data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def print_list(self, val):
        while(val is not None):
            print(val.data)
            val = val.next


llist = DoubLinkedList()
llist.push(2)
llist.push(4)
llist.push(8)
llist.push(10)


print("\nOriginal Linked List")
llist.print_list(llist.head)


llist.reverse()

print("\n Reversed Linked List")
llist.print_list(llist.head)
