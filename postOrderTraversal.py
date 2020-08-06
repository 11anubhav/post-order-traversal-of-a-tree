# python3 is used as a programming language
#Without Recurrsion Solution for postorder traversal of a BST
class newNode: 

	# Constructor to create a newNode 
    # visited is used as a flag
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
		self.visited = False

def postorder(head) : 

	temp = head 
	while (temp and temp.visited == False): 

		# Visited left subtree 
		if (temp.left and
			temp.left.visited == False): 
			temp = temp.left 

		# Visited right subtree 
		elif (temp.right and
			temp.right.visited == False): 
			temp = temp.right 

		# Print node 
		else: 
			print(temp.data, end = " ") 
			temp.visited = True
			temp = head 
						

if __name__ == '__main__': 

	root = newNode(9) 
	root.left = newNode(2) 
	root.right = newNode(11) 
	root.left.left = newNode(1) 
	root.left.right = newNode(6) 
	root.left.right.left = newNode(4) 
	root.left.right.right = newNode(7) 
	root.right.right = newNode(17) 
	root.right.right.left = newNode(12) 
	postorder(root) 
