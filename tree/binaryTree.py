#搜索二叉树的有关操作

class Node:
    """定义节点"""
    def __init__(self,value,parent=None,left=None,right=None):
        self.parent=parent
        self.left=left
        self.right=right
        self.value=value

    def __repr__(self):
        return str(self.value)

def inorder_tree_walk1(node:Node):
    """递归从某一节点开始进行中序遍历"""
    if node is None:
        return 
    inorder_tree_walk1(node.left)
    print(node.value)
    inorder_tree_walk1(node.right)

def inorder_tree_walk2(node:Node):
    """用栈实现中序遍历"""
    if node is None:
        return
    stack=[]
    while len(stack)!=0 or node is not None:
        if node is not None:
            stack.append(node)
            node=node.left
        else:
            node=stack.pop()
            print(node.value)
            node=node.right

def tree_search1(root:Node,value):
    """给定搜索二叉树的根节点，以及查找的值，递归进行搜索"""
    if root is None or value == root.value:
        return root
    if value <= root.value:
        root = tree_search1(root.left,value)
    else:
        root = tree_search1(root.right,value)   
    return root        

def tree_search2(root:Node,value):
    """给定搜索二叉树的根节点，以及查找的值，非递归进行搜索"""
    while root is not None and root.value != value:
        if value < root.value:
            root=root.left
        else:
            root=root.right
    return root

def tree_minimum(root:Node):
    """给定根节点，求搜索二叉树的最小节点"""
    while root.left is not None:
        root=root.left
    return root

def tree_maxmum(root:Node):
    """给定根节点，求搜索二叉树的最大节点"""
    while root.right is not None:
        root=root.right
    return root

def tree_successor(node:Node):
    """求某一节点的中序遍历的后继节点"""
    if node.right is not None:
        node=node.right
        while node.left is not None:
            node=node.left
        return node
    parent=node.parent
    while parent is not None and parent.left is not node:
        node=parent
        parent=node.parent
    return parent

def tree_insert(root:Node,node:Node):
    """二叉查找树插入操作"""
    parent=None
    while root is not None:
        if root.value >= node.value:
            parent=root
            root=root.left
        else:
            parent=root
            root=root.right
    root=node
    root.parent=parent
    if parent is not None:
        if parent.value >= node.value:
            parent.left=node
        else:
            parent.right=node

def treee_delete(root:Node,node:Node):
    """从搜索二叉树中删除某个存在的节点"""
    if node.left is None or node.right is None:
        y=node
    else:
        y=tree_successor(node)
    if y.left is not None:
        x = y.left
    else:
        x = y.right
    if x is not None:
        x.parent = y.parent
    if y.parent is None:
        root=x
    elif y is y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x
    if y is not node:
        node.value=y.value
    return y

#test    
node15=Node(15)
arr=[5,16,3,12,20,10,13,18,23,6,7]
for i in arr:
    node=Node(i)
    tree_insert(node15,node)
#inorder_tree_walk1(node15)
inorder_tree_walk2(node15)
a=tree_search2(node15,5)
print(a," ",a.parent)
b=tree_minimum(node15)
c=tree_maxmum(node15)
d=tree_successor(a)
print(d)
e=treee_delete(node15,a)
print()

