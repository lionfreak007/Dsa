class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkeList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


  #  def append(self, new_data):
  #      new_node = Node(new_data)
  #      new_node.next = self.head

 #   if self.head is None:
 #       self.head = new_node
        #return

#    last = self.head
 #   while(last.next):
 #       last = last.next

 #   last.next = new_node   

    def deleteNode(self, val):
    
        temp = self.head


        while temp is not None:
            if(temp.data == val):
                break
            prev = temp
            temp = temp.next

    

        prev.next = temp.next
        temp = None

    
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
    llist = LinkeList()
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
 #   llist.append(6)


print ("Linkedlist is : ")
llist.printList()

llist.deleteNode(2)
print ("Deleted Node ")
llist.printList()

llist.reverse()
print("Linkedlist iterative method")
llist.printList()

llist.reverse_()
print("LinkedList usoing recursive method")
llist.printList()


