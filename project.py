# algo for leaf count

#getLeafCount(node)
#1) If node is NULL then return 0.
#2) Else If left and right child nodes are NULL return 1.
#3) Else recursively calculate leaf count of the tree using below formula.
    #Leaf count of a tree = Leaf count of left subtree + 
     #                            Leaf count of right subtree



# algo for bfs
# printLevelorder(tree)
#1) Create an empty queue q
#2) temp_node = root /*start from root*/
#3) Loop while temp_node is not NULL
 #   a) print temp_node->data.
  #  b) Enqueue temp_node’s children (first left then right children) to q
  # c) Dequeue a node from q and assign it’s value to temp_node


# algo for dfs 
# Algorithm Preorder(tree)
   #1. Visit the root.
   #2. Traverse the left subtree, i.e., call Preorder(left-subtree)
   #3. Traverse the right subtree, i.e., call Preorder(right-subtree)  