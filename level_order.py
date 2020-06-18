# Program to print level order traversal using Python

# We use a queue here to store the elements in FIFO order
# where there is a trade-off in space for reducing time complexity 
  
# Binary Tree node constructor
class Node: 
    # Function to create a new node 
    def __init__(self ,value): 
        self.data = value 
        self.left = None
        self.right = None
  
# Function that prints level order traversal of a binary tree 
def printLevelOrder(root): 
    # Base Case 
    if root is None: 
        return
      
    # Initialize a queue for storing nodes in FIFO order 
    queue = [] 
  
    # Enqueue Root
    # This the point we start enqueuing and the function stops when the queue is empty again 
    queue.append(root) 

    # The function terminates when the queue is empty again

    while(len(queue) > 0): 
        # Print the element at the top of queue and then dequeue it 
        print (queue[0].data) 
        node = queue.pop(0) 
  
        # Enqueue left child of the element that has been dequeued
        if node.left is not None: 
            queue.append(node.left) 
  
        # Enqueue right child of the element that has been dequeued
        if node.right is not None: 
            queue.append(node.right) 
  
# Driver Program
# We create a binary tree as given in the question
root = Node(1) 
root.right = Node(2)  
root.right.right = Node(5)
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.right = Node(4)  

#Expected output is : 1 -> 2 -> 5 -> 3 -> 6 -> 4.
  
print ("Level Order Traversal of the given binary tree is : ") 
printLevelOrder(root)