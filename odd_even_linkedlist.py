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


def odd_even_linkedlist(ll_head):
    curr_odd = ll_head
    curr_even = ll_head.next

    odd_head = curr_odd
    even_head = curr_even
    last_odd_node = None
    while(curr_odd != None):
        last_odd_node = curr_odd

        if(curr_even == None):
            break
        curr_odd.next = curr_even.next
        curr_odd = curr_odd.next

        if(curr_odd == None):
            break
        curr_even.next = curr_odd.next
        curr_even = curr_even.next

    last_odd_node.next = even_head
    return odd_head


if __name__ == "__main__":
    input_linked_list = input("Enter Linked List: ")
    list_array = input_linked_list.split('->')
    ll_head = create_linked_list(list_array)
    merged_ll = odd_even_linkedlist(ll_head)
    print_nodes(merged_ll)
