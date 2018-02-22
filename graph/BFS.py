#广度优先算法

#定义图节点模型,临接表表示
class Node:

    def __init__(self,value,adjacentSet=None):
        """
        value:节点的值
        adjacentSet:领接表
        """
        self.value=value
        self.adjacentSet=adjacentSet
    
    def __repr__(self):
        return 'Node{}'.format(self.value)


import sys
from queue import Queue
#广度优先算法
def BFS(vertexSet:set,node:Node):
    """
    vertexSet:图定点的集合
    node:源节点
    vertexAttribute存储节点的额外属性
    color属性:0-->white,1-->gray,2-->black
    distance属性-->遍历到该节点，走过的距离
    parient属性-->存放遍历时，该节点的直接前驱节点
    """
    vertexAttribute={v:{'color':0,'distance':sys.maxsize,'parent':None} for v in vertexSet}
    vertexAttribute[node]['color']=1
    vertexAttribute[node]['distance']=0
    vertexAttribute[node]['parent']=None
    q=Queue()
    q.put(node)
    while not q.empty():
        u=q.get()
        print(u)
        for v in u.adjacentSet:
            if vertexAttribute[v]['color'] == 0:
                vertexAttribute[v]['color']=1
                vertexAttribute[v]['distance']=vertexAttribute[u]['distance']+1
                vertexAttribute[v]['parent']=u
                q.put(v)
        vertexAttribute[u]['color']=2
    return vertexAttribute

#输出从s-->v的最短路径上的所有节点

def print_path(vertextSet,s:Node,v:Node):
    if v is s:
        print(s)
    else:
        vertexAttribute=BFS(vertexSet,s)
        if vertexAttribute[v]['parent'] is None:
            print('no path from {} to {}'.format(s,v))
        else:
            print_path(vertexSet,s,vertexAttribute[v]['parent'])
            print(v)
#test
node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)
node1.adjacentSet={node1,node2,node5}#{node2,node5}
node2.adjacentSet={node1,node5,node3,node4}#{node5,node3,node4}
node3.adjacentSet={node2,node4}
node4.adjacentSet={node3,node2,node5}
node5.adjacentSet={node4,node1,node2}#{node4,node2}
vertexSet={node1,node2,node3,node4,node5}

vertexAttribute=BFS(vertexSet,node1)
#print_path(vertexSet,node1,node1)
print('----')
