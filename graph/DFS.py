#深度优先算法

#定义图节点模型,领接表表示
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

from time import perf_counter
#访问某一个节点
def DFS_visit(vertexAttribute,node:Node):
    vertexAttribute[node]['color']=1
    global time
    time+=1
    vertexAttribute[node]['initTime']=time
    for v in node.adjacentSet:
        if vertexAttribute[v]['color'] == 0:
            vertexAttribute[v]['parent']=node
            DFS_visit(vertexAttribute,v)
    vertexAttribute[node]['color']=2
    time+=1
    vertexAttribute[node]['leaveTime']=time
    print(node)


#深度优先算法
def DFS(vertexSet):
    #所有节点属性初始化
    #color:0--->未访问，1：待访问，2：已访问
    global time
    time=0
    vertexAttribute={v:{'color':0,'initTime':0,'leaveTime':0,'parent':None} for v in vertexSet}
    for v in vertexSet:
        if vertexAttribute[v]['color'] == 0:
            DFS_visit(vertexAttribute,v)
    return vertexAttribute

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

vertexAttribute=DFS(vertexSet)
print('___')