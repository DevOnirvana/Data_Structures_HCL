# The algorithm is based on finding a path from root node to the given nodes
# We then store the paths in a list for both the given nodes
# We then traverse the list to find the nearest two commoon ancestors/parents

class Node: 
    # Binary Tree Node
    def __init__(self, value): 
        self.value =  value 
        self.left = None
        self.right = None

# This function finds the path from root to the given node if it exists
def findPath( root, path, k): 
  
    # Base Case 
    if root is None: 
        return False
  
    # This node is stored in a python list 'path'(vector).
    path.append(root.value) 
  
    # CHeck if k is same as the root's value 
    if root.value == k : 
        return True
  
    # Check if k is there in left sub-tree or right sub-tree 
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right!= None and findPath(root.right, path, k))): 
        return True 
  
    # If node is not present in sub-tree with root as root, 
    # pop root from path and return False, it means the node is mising
       
    path.pop() 
    return False
  
# Returns nearest common parents if node n1 , n2 are present in the given 
# binary tre otherwise return -1 
def findNearestCommonParents(root, n1, n2): 
  
    # initialize list(vector) to store path from root to given nodes 
    path1 = [] 
    path2 = [] 
  
    # Find paths from root to n1 and root to n2. 
    # If either n1 or n2 is not present , return -1  
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)): 
        return -1 
  
    # Compare the paths to get the first different value say x in the list
    # At this point, the two previous elements of x in the paths will give us the answer
    i = 0 
    while(i < len(path1) and i < len(path2)): 
        if path1[i] != path2[i]: 
            break
        i += 1
    #returns a list of the nearest two common ancestors if there
    return [path1[i-1], path1[i-2]] if (i-2)>=0 else [path1[i-1]] # here (i-2) >= 0 indicates if there is a second nearest 
                                                                # common ancestor else returns the only nearest ancestor
  
  
# Driver program to test above function 

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 

a = int(input('Enter first node'))
b = int(input('Enter second node'))
  
print(findNearestCommonParents(root, a, b,))