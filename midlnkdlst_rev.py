class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, new_data):
        new_node = Node(new_data)

        if(self.head) == None:
            self.head = new_node
            self.last = new_node

        else:
            self.last.next = new_node
            self.last = new_node

    def middle_element(self):
        cur = self.head
        count = 0
        while(cur):
            count += 1
            cur = cur.next
        mid = count // 2
        cur = self.head
        for temp in range(mid):
            cur = cur.next
        return cur

    def printlist(self):
        temp = self.head
        while(temp):
            print(" %d " % (temp.data))
            temp = temp.next


if __name__ == "__main__":
    llist = Linkedlist()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.append(5)

print("Linkedlist")
llist.printlist()

llist.middle_element()
print("New Linkedlist")
llist.printlist()
