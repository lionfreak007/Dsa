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

    def printList(self):
        temp = self.head
        while(temp):

            print(" %d " % (temp.data)),
            temp = temp.next


    def deleteNode(self, key):  
          
        
        temp = self.head  
  
       
        if (temp is not None):  
            if (temp.data == key):  
                self.head = temp.next
                temp = None
                return
  
        
        while(temp is not None):  
            if temp.data == key:  
                break
            prev = temp  
            temp = temp.next
  
        
        if(temp == None):  
            return
  
         
        prev.next = temp.next
  
        temp = None


if __name__ == '__main__':
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.append(5)
    llist.append(6)

    print("Linkedlist is : ")
    llist.printList()


    llist.deleteNode(6)
    print("Deleted key")
    llist.printList()

    

