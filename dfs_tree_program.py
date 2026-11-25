# DFS methods in tree program


# Returns a label for each letter, like A1 and A2 when a letter repeats
def make_labels(name):
    labels = []
    seen = {}
    for letter in name:
        seen[letter] = seen.get(letter, 0) + 1
        if name.count(letter) > 1:
            labels.append(letter + str(seen[letter]))
        else:
            labels.append(letter)
    return labels


# A node holds one label and links to its left and right child
class Node:
    # Creates a node with no children
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# A binary tree with the three DFS methods
class BinaryTree:
    # Creates an empty tree
    def __init__(self):
        self.root = None

    # Adds a node in the first empty spot, level by level, left to right
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left is None:
                current.left = new_node
                return
            queue.append(current.left)
            if current.right is None:
                current.right = new_node
                return
            queue.append(current.right)

    # Preorder: Root -> Left -> Right
    def preorder(self, node, order):
        if node is not None:
            order.append(node.data)
            self.preorder(node.left, order)
            self.preorder(node.right, order)

    # Inorder: Left -> Root -> Right
    def inorder(self, node, order):
        if node is not None:
            self.inorder(node.left, order)
            order.append(node.data)
            self.inorder(node.right, order)

    # Postorder: Left -> Right -> Root
    def postorder(self, node, order):
        if node is not None:
            self.postorder(node.left, order)
            self.postorder(node.right, order)
            order.append(node.data)


# Builds the tree from the first and last name, then shows the DFS methods
def run():
    first = input("Enter your first name: ").upper()
    last = input("Enter your last name: ").upper()
    name = first + last
    if name == "":
        print("Name cannot be empty.")
        return

    tree = BinaryTree()

    # Add each letter to the tree
    labels = make_labels(name)
    for label in labels:
        tree.insert(label)

    print("\nLetters added:", " ".join(labels))

    # Preorder
    order = []
    tree.preorder(tree.root, order)
    print("\nPreorder  (Root -> Left -> Right):", " -> ".join(order))

    # Inorder
    order = []
    tree.inorder(tree.root, order)
    print("Inorder   (Left -> Root -> Right):", " -> ".join(order))

    # Postorder
    order = []
    tree.postorder(tree.root, order)
    print("Postorder (Left -> Right -> Root):", " -> ".join(order))


if __name__ == "__main__":
    run()