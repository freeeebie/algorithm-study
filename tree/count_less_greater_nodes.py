
class BST:
    class Node:
        def __init__(self, left, right, value, leftchildren, rightchildren):
            self.left = left
            self.right = right
            self.value = value
            self.leftchildren = leftchildren
            self.rightchildren = rightchildren

    def __init__(self):
        self.root = None

    def insert(self, value):
        node = self.Node(None, None, value, 0, 0)
        if self.root == None:
            self.root = node
        else:
            self.insertwithnode(self.root, value, node)

    def insertwithnode(self, node, value, newnode):
        if node == None:
            node = newnode
        else:
            if node.value > value:
                if node.left is not None:
                    self.insertwithnode(node.left, value, newnode)
                else:
                    node.left = newnode
                node.leftchildren += 1
            else:
                if node.right is not None:
                    self.insertwithnode(node.right, value, newnode)
                else:
                    node.right = newnode
                node.rightchildren += 1

    def inorderprint(self, node):
        if not node:
            return
        self.inorderprint(node.left)
        print(node.value)
        self.inorderprint(node.right)

def count_less(node, input, count):
    if node is None:
        return count
    if node.value > input:
        count += count_less(node.left, input, count)
    elif node.value < input:
        count += node.leftchildren + 1 + count_less(node.right, input, count)
    elif node.value == input:
        count += node.leftchildren
    return count

def count_more(node, input, count):
    if node is None:
        return count
    if node.value < input:
        count += count_more(node.right, input, count)
    elif node.value > input:
        count += node.rightchildren + 1 + count_more(node.left, input, count)
    elif node.value == input:
        count += node.rightchildren
    return count


tree = BST()
tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(45)
tree.insert(80)
tree.insert(60)
tree.insert(70)
tree.insert(100)
tree.insert(90)
tree.insert(150)
tree.insert(180)
tree.inorderprint(tree.root)
lesscount = 0
lesscount = count_less(tree.root, 80, lesscount)
print(lesscount)
morecount = 0
print(count_more(tree.root, 80, morecount))

