#B树
#B树与红黑树类似，但在降低磁盘I/O操作次数方面要更好。
#B树与红黑树的不同在于，B树的节点可以有很多子女。
#如果某一节点有n(x)个关键字，则该节点就有n(x)+1个子女
#B树度的概念：每个节点能包含的关键字数有一个上界和下界。
#每个非根节点必须至少包含t-1个关键字。每个非根的内节点至少有t个子女。如果树是非空的，则根节点至少包含一个关键字。
#每个节点可包含至多2t-1个关键字，所以一个内节点至多有2t个子女。
#------节点的特性------
#每个节点有以下域
"""
n(x)---->当前存储在节点x中的关键字数
n(x)个关键字本身，以非降序存放
leaf(x)是一个布尔值，表明是否是叶子节点
每个节点还包含n(x)+1个指向其子女的指针
各关键字对存储在各子数中的关键字范围进行分隔
每个叶子节点具有相同的高度，即树的高度
"""
class Bnode:

    def __init__(self,subNodeList=None,leaf=False,keyValue=None):
        self.subNodeList=subNodeList
        self.leaf=leaf
        self.keyValue=keyValue
        self.size=len(keyValue)
        self.key_subNode_map=self.subNodeListSplict(self.keyValue,self.subNodeList)

    def __repr__(self):
        return str(self.keyValue)
    
    def subNodeListSplict(self,keyValue,subNodeList):
        """
        根据keyValue和subNodeList建立一个映射，将subNodeList进行一个划分
        """
        key_subNode_map={}
        j=0
        for key in keyValue:
            while j < len(subNodeList) and subNodeList[j]<= key:
                j+=1
            j-=1
            
            key_subNode_map[key]=j
        return key_subNode_map

    def findsubNode(self,i):



def BtreeSearch(root:Bnode,key):
    i=0
    while i < root.size and key > root.keyValue[i]:
        i=i+1
    if i < root.size and key == root.keyValue[i]:
        return tuple(root,i)
    if root.leaf:
        return None
    else:
        return BtreeSearch(root.subNodeList,key)
