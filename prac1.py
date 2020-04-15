# binary tree - A , A->B A-> C , B->D , B->E , C-> F
# leaf node-> D,E,F
# bfs-> A - B -C - D - E -F
# DFS- > A - B- D- E -C-F


class Node:
# How the binary tree will look like 
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# code to implement Breadth first search

    def breadthFirstSearch(root):
        if root is None:
            return

        queue = []
        queue.append(root)

        while(le(queue) > 0):
            print queue[0].data
            node = queue.pop(0)

        if node.left != None:
            queue.append(node.left)

        if node.right != None:
            queue.append(node.right)


# code to implement depth first search

    def depthFirstSearch(root):
        if root:
            print(root.data)

            print depthFirstSearch(root.left) 

            print depthFirstSearch(root.right)                                    


# coode to count leaf of  the tree
    def countLeaves(node):
        if node == null:
            return 0

        elif node.left == None and node.right == None :

            return 1

        else:
            return countLeaves(node.left) + countLeaves(node.right)





# setup a tree


    root = Node(A)
    root.left = Node(B)
    root.right = Node(C)
    root.left.left = Node(D)
    root.left.right = Node(E)
    root.right.left = Node(F)

print "Breadth First search of the tree is : " breadthFirstSearch(root)'\n'

print "Depth First search of the tree is : " depthFirstSearch(root)'\n'

print "leaf count of the tree is : " (countLeaves(root)) 