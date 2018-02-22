#红黑树
"""
红黑树是一颗搜索二叉树
每个节点是红的或者黑的
根节点是黑色的
每个叶子节点是黑色的(NIL节点)
如果一个节点是红色的，则他的两个儿子都是黑色的
对每一个节点，从该节点到该子孙节点的所有路径上包含相同数目的黑色节点(黑高度相同)--->保证了平衡性
"""

#定义红黑树的节点
class Node:
    #默认为NIL叶子节点，color:0-->black,1-->red
    def __init__(self,value=None,color=0,parent=None,left=None,right=None):
        self.value=value
        self.color=color
        self.parent=parent
        self.left=left
        self.right=right

    def __repr__(self):
        s='black' if self.color == 0 else 'red'
        v=self.value if self.value is not None else 'NIL'
        return '{} node{}'.format(s,v)

#左旋操作
def left_rotate(root:Node,node:Node):
    r=node.right
    node.right=r.left
    if r.left.value is not None:
        r.left.parent=node
    r.parent=node.parent
    if node.parent.value is None:
        root=r
    elif node is node.parent.left:
        node.parent.left=r 
    else:
        node.parent.right=r 
    r.left=node
    node.parent=r
    return root

#右旋
def right_rotate(root:Node,node:Node):
    l=node.left
    node.left=l.right
    if l.right.value is not None:
        l.right.parent=node
    l.parent=node.parent
    if node.parent.value is None:
        root=l
    elif node is node.parent.left:
        node.parent.left=l
    else:
        node.parent.right=l
    l.right=node
    node.parent=l
    return root

#插入操作保持红黑树的性质
def rb_insert_fix(root:Node,z:Node):
    while z.parent.color == 1:
        if z.parent is z.parent.parent.left:
            y=z.parent.parent.right
            if y.color == 1:
                z.parent.color=0
                y.color=0
                z.parent.parent.color=1
            elif z is z.parent.right:
                z=z.parent
                root=left_rotate(root,z)
            z.parent.color=0
            z.parent.parent.color=1
            root=right_rotate(root,z.parent.parent)
        else:
            y=z.parent.parent.left
            if y.color == 1:
                z.parent.color=0
                y.color=0
                z.parent.parent.color=1
            elif z is z.parent.left:
                z=z.parent
                root=right_rotate(root,z)
            z.parent.color=0
            z.parent.parent.color=1
            root=left_rotate(root,z.parent.parent)
    root.color=0
    return root
    
#红黑树插入
def rb_insert(root:Node,z:Node):
    y=Node()
    x=root
    while x.value is not None:
        y=x
        if z.value <= x.value:
            x=x.left
        else:
            x=x.right
    z.parent=y
    if y.value is None:
        root=z
    elif z.value <= y.value:
        y.left=z
    else:
        y.right=z
    z.left=Node(parent=z)
    z.right=Node(parent=z)
    z.color=1
    root=rb_insert_fix(root,z)
    return root

#红黑树删除保持性质
def rb_delete_fix(root:Node,x:Node):
    while x is not root and x.color == 0:
        if x is x.parent.left:
            w=x.parent.right
            if w.color == 1:
                w.color=0
                x.parent.color=1
                root=left_rotate(root,x.parent)
                w=x.parent.right
            if w.value is None:return root
            if w.left.color == 0 and w.right.color == 0:
                w.color=1
                x=x.parent
            elif w.right.color == 0:
                w.left.color=0
                w.color=1
                root=right_rotate(root,w)
                w=x.parent.right
            w.color=x.parent.color
            x.parent.color=0
            w.right.color=0
            root=left_rotate(root,x.parent)
            x=root
        else:
            w=x.parent.left
            if w.color == 1:
                w.color=0
                x.parent.color=1
                root=right_rotate(root,x.parent)
                w=x.parent.left
            if w.left.color == 0 and w.right.color == 0:
                w.color=1
                x=x.parent
            elif w.right.color == 0:
                w.right.color=0
                w.color=1
                root=left_rotate(root,w)
                w=x.parent.left
            w.color=x.parent.color
            x.parent.color=0
            w.left.color=0
            root=right_rotate(root,x.parent)
            x=root
    x.color=0
    return root

#求红黑树某一节点的中序遍历的后继节点
def tree_successor(node:Node):
    """求某一节点的中序遍历的后继节点"""
    if node.right.value is not None:
        node=node.right
        while node.left.value is not None:
            node=node.left
        return node
    parent=node.parent
    while parent.value is not None and parent.left is not node:
        node=parent
        parent=node.parent
    return parent

#红黑树的删除操作
def rb_delete(root:Node,z:Node):
    if z.left.value is None or z.right.value is None:
        y=z
    else:
        y=tree_successor(z)
    if y.left.value is not None:
        x=y.left
    else:
        x=y.right
    x.parent=y.parent
    if y.parent.value is None:
        root=x
    elif y is y.parent.left:
        y.parent.left=x
    else:
        y.parent.right=x
    if y is not z:
        z.value=y.value
    if y.color==0:
        root=rb_delete_fix(root,x)
    return root

#红黑树的搜索
def rb_search(root:Node,x):
    if root is None or root.value == x :
        return root
    if root.value > x:
        root = rb_search(root.left,x)
    else:
        root = rb_search(root.right,x)
    return root

#红黑树中序遍历
def rb_inorder(root:Node):
    if root.value is None:
        return root
    rb_inorder(root.left)
    print(root,'-->',end=' ')
    rb_inorder(root.right)
    print('---')      

#插入测试
node11=Node(11)
node2=Node(2)
node14=Node(14)
node1=Node(1)
node7=Node(7)
node15=Node(15)
node5=Node(5)
node8=Node(8)
node4=Node(4)
node3=Node(3)
node6=Node(6)
node20=Node(20)
node9=Node(9)
node16=Node(16)
root=Node()
root=rb_insert(root,node11)
root=rb_insert(root,node2)
root=rb_insert(root,node14)
root=rb_insert(root,node1)
root=rb_insert(root,node5)
root=rb_insert(root,node16)
root=rb_insert(root,node7)
root=rb_insert(root,node3)
root=rb_insert(root,node6)
root=rb_insert(root,node20)
root=rb_insert(root,node9)
root=rb_insert(root,node15)
rb_inorder(root)
root=rb_delete_fix(root,node6)
node=rb_search(root,5)
print(node)
print('end')

