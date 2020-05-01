class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():

    def __init__(self):
        self.head = None
        self.last = None

    def append(self,new_data):
        new_node = Node(new_data)

        if(self.head == None):
            self.head = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def node_evenoodd(self,head):

        if(self.head == None):
            return None

        even = self.head
        odd = self.head.next


        firstele = even

        

        




    def printList(self):
        temp = self.head
        while(temp):
            print(" %d " % (temp.data)),
            temp = temp.next

if __name__=='__main__':
    llist = LinkedList()
    llist.append(10)
    llist.append(20)
    llist.append(30)
    llist.append(40)
    llist.append(50)


    print("Linked list is : ")
    llist.printList()
        


        
