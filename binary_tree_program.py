# Binary tree program


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


# A binary tree where each node has at most two children
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

    # BFS: visits the nodes level by level using a queue
    def bfs(self):
        order = []
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            order.append(current.data)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return order

    # DFS preorder: root, then left, then right
    def preorder(self, node, order):
        if node is not None:
            order.append(node.data)
            self.preorder(node.left, order)
            self.preorder(node.right, order)

    # DFS inorder: left, then root, then right
    def inorder(self, node, order):
        if node is not None:
            self.inorder(node.left, order)
            order.append(node.data)
            self.inorder(node.right, order)

    # DFS postorder: left, then right, then root
    def postorder(self, node, order):
        if node is not None:
            self.postorder(node.left, order)
            self.postorder(node.right, order)
            order.append(node.data)

    # Shows the left and right child of every node
    def display(self):
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            left = current.left.data if current.left else "None"
            right = current.right.data if current.right else "None"
            print(current.data, "-> left:", left, "| right:", right)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)


# Builds a binary tree from the name, then shows BFS and DFS
def run():
    name = input("Enter your last name: ").upper()
    if name == "":
        print("Name cannot be empty.")
        return

    tree = BinaryTree()

    # Add each letter to the tree
    for label in make_labels(name):
        tree.insert(label)

    print("\n--- Binary Tree ---")
    tree.display()

    # BFS
    print("\n--- BFS (level order) ---")
    print(" ".join(tree.bfs()))

    # DFS
    print("\n--- DFS ---")
    order = []
    tree.preorder(tree.root, order)
    print("Preorder :", " ".join(order))

    order = []
    tree.inorder(tree.root, order)
    print("Inorder  :", " ".join(order))

    order = []
    tree.postorder(tree.root, order)
    print("Postorder:", " ".join(order))


if __name__ == "__main__":
    run()
