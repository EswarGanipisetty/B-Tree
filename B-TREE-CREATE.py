class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, t):
        self.root = BTreeNode()
        self.t = t

    def create(self, keys):
        if not keys:
            return None

        if len(keys) > (2 * self.t) - 1:
            raise ValueError("Number of keys exceeds node capacity")

        self.root.keys = sorted(keys)
        if len(keys) > 1:
            self.root.leaf = False
            self.root.children.append(BTreeNode())
            self.root.children.append(BTreeNode())
            self.root.children[0].keys = self.root.keys[:self.t - 1]
            self.root.children[1].keys = self.root.keys[self.t:]
        return self.root

    def print_tree(self, node=None, level=0):
        node = node or self.root
        print("Level", level, ": ", node.keys)
        if not node.leaf:
            for child in node.children:
                self.print_tree(child, level + 1)

# Example usage:
keys = [10, 20, 30, 40, 50]
btree = BTree(3)  # B-tree with order 2
btree.create(keys)
btree.print_tree()
