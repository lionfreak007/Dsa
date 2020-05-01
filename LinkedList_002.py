class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, new_data):
        new_node = Node(new_data)

        if(self.head == None):
            self.head = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    
    def reverse(self):  # using loops / iterattion
        prev = None
        cur = self.head
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def reverse_recr(self , cur, prev):
        if cur.next is None:
            self.head = cur

            cur.next = prev
            return

        next = cur.next
        cur.next = prev

        self.reverse_recr(next, cur)

    def reverse_(self):
        if self.head is None:
            return
        self.reverse_recr(self.head , None)


    def printList(self):
        temp = self.head
        while(temp):
            print(" %d " % (temp.data)),
            temp = temp.next

if __name__=='__main__':
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.append(5)
 #   llist.append(6)


print ("Linkedlist is : ")
llist.printList()


llist.reverse()
print("Linkedlist iterative method")
llist.printList()

llist.reverse_()
print("LinkedList usoing recursive method")
llist.printList()


