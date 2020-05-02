class Node:
    def __init__(self, node_val):
        self.val = node_val
        self.next = None


def create_linked_list(array):
    head = None
    curr_node = None
    for node_val in array:
        if(not(head)):
            head = Node(node_val)
            curr_node = head
        else:
            curr_node.next = Node(node_val)
            curr_node = curr_node.next

    return head


def print_nodes(ll_head):
    curr_node = ll_head
    while(curr_node.next):
        print(curr_node.val, end="->")
        curr_node = curr_node.next
    print(curr_node.val, end="\n")


if __name__ == "__main__":
    input_linked_list = input("Enter Linked List: ")
    list_array = input_linked_list.split('->')
    ll_head = create_linked_list(list_array)
    print_nodes(ll_head)
