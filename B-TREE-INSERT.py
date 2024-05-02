class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, t):
        self.root = BTreeNode()
        self.t = t

    def insert(self, key):
        if len(self.root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode(leaf=False)
            new_root.children.append(self.root)
            self.split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            node.keys.insert(i + 1, key)
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def split_child(self, parent, index):
        t = self.t
        child = parent.children[index]
        new_child = BTreeNode(leaf=child.leaf)
        parent.keys.insert(index, child.keys[t - 1])
        parent.children.insert(index + 1, new_child)
        new_child.keys = child.keys[t: (2 * t) - 1]
        child.keys = child.keys[0: t - 1]
        if not child.leaf:
            new_child.children = child.children[t: (2 * t)]
            child.children = child.children[0: t]

    def print_tree(self, node=None, level=0):
        node = node or self.root
        print("Level", level, ": ", node.keys)
        if not node.leaf:
            for child in node.children:
                self.print_tree(child, level + 1)

# Example usage:
btree = BTree(2)  # B-tree with order 2
keys = [10, 20, 30, 40, 50]
for key in keys:
    btree.insert(key)
btree.print_tree()
