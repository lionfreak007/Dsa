class Node:

    def __init__(self, value):
        self.value = value
        self.next = None



class Linkedlist:
    def __init__(self):
        self.head = None

# Function to insert new data into list

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head =new_node

# Method to remove element from the list ie. defined as val
 
    def remove (self,val):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.get_data() == val:   #getter
                if prev_node is not None:
                    prev_node.set_next(this_node.get_next())   #setter

                else:
                    self.root = this_node.get_next()
                self.size == -1
                return True  # node removed

            else:
                prev_node = this_node
                this_node = this_node.get_next()
            return False  # No data found condition

# reverse element (iterative)

    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr:             #loop is used in iteration to reach the last element
            nxt = cur.next
            curr.next = prev

            self.rev_ele(prev,"PREV")
            self.rev_ele(curr,"CURR")
            self.rev_ele(nxt,"NXT")

            prev = curr
            curr = nxt
            self.head = prev

    def reverse_recursive(self):

        def rev_rec(curr, prev):   # method call itself  to reach the last element
            if not curr:
                return prev

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            return rev_rec(curr, prev)

        self.head = rev_rec(curr = self.head , prev = None)


# inserting elements into linked list
if __name__ == "__main__":
    llist = Linkedlist()
    llist.push("A")
    llist.push("B")
    llist.pish("C")
    llist.push("D")
    llist.push("E")
    llist.push("F")


llist.remove()



