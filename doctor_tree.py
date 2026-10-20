class DoctorNode:
    def __init__(self, value): 
        self.value = value 
        self.left = None 
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, employee_name, side, current_node=None):
        
        if self.root is None:
            print("Tree is empty.")
            return
    
        if current_node is None:
            current_node = self.root 
    
        if current_node.value == parent_name: 
            if side == "left" and current_node.left is None: 
                current_node.left = DoctorNode(employee_name) 
                print(f"{employee_name} added under {parent_name} on the left.") 
                return True 
            elif side == "right" and current_node.right is None: 
                current_node.right = DoctorNode(employee_name) 
                print(f"{employee_name} added under {parent_name} on the right.") 
                return True 
            else: 
                print(f"{parent_name} already has a {side} subordinate.") 
            return True
    
        found_left = False
        found_right = False
    
        if current_node.left:
            found_left = self.insert(parent_name, employee_name, side, current_node.left)
    
        if current_node.right and not found_left:
            found_right = self.insert(parent_name, employee_name, side, current_node.right)
    
        if not(found_left or found_right):
            if current_node == self.root:
                print(f"Doctor {parent_name} not found in the tree.")
            return False
    
        return True

    def preorder(self, node):
        if node is None: # Base case, we've reached a leaf
            return []
        
        result = [node.value]
        result += self.preorder(node.left)
        result += self.preorder(node.right)

        return result

    def inorder(self, node):
        if node is None: # Base case, we've reached a leaf
            return []

        result = []
        result += self.preorder(node.left)
        result.append(node.value)
        result += self.preorder(node.right)

        return result

    def postorder(self, node):
        if node is None: # Base case, we've reached a leaf
            return []

        result = []
        result += self.preorder(node.left)
        result += self.preorder(node.right)
        result.append(node.value)

        return result


example_tree = DoctorTree()
example_tree.root = DoctorNode("A")
example_tree.insert("A", "B", "left")
example_tree.insert("A", "C", "right")
example_tree.insert("B", "D", "left")
example_tree.insert("B", "E", "right")
example_tree.insert("C", "F", "right")

print(example_tree.preorder(example_tree.root))
print(example_tree.inorder(example_tree.root))
print(example_tree.postorder(example_tree.root))