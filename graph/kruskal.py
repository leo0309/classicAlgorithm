#最小生成树算法(kruskal实现)

#定义节点
class Node:
    def __init__(self,name):
        self.name=name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return 'Node %s' %self.name


#定义权重边
class vertex:
    def __init__(self,node1:Node,node2:Node,weight=0):
        """node1,node2:节点元素,weight:边的权值，0代表直接通过"""
        self.node1=node1
        self.node2=node2
        self.weight=weight

    #定义hash函数
    def __hash__(self):
        return hash(self.node1) & hash(self.node2)

    def __repr__(self):
        return '({},{})'.format(self.node1.name,self.node2.name)

def find_set(Nodesets:list,node:Node):
    for nodeset in Nodesets:
        if node.name in nodeset:
            return nodeset
    return None
    

def kruskal(Nodesets:list,vertexlist:list):
    """Nodeset:节点集合，vertexset:边集合,result:结果集"""
    result=set()
    vertexlist.sort(key=lambda x: x.weight)
    for vertex in vertexlist:
        nodeset1=find_set(Nodesets,vertex.node1)
        nodeset2=find_set(Nodesets,vertex.node2)
        if not nodeset1 is nodeset2:
            result.add(vertex)
            Nodesets.append(nodeset1.union(nodeset2))
            Nodesets.remove(nodeset1)
            Nodesets.remove(nodeset2)
    return result

#test
Nodelist=[]
Nodesets=[]
for i in range(9):
    Nodelist.append(Node(chr(ord('a')+i)))
    Nodesets.append(set(Nodelist[i].name))
w=[4,8,7,9,10,2,1,7]
vertexlist=[]
for i in range(8):
    vertexlist.append(vertex(Nodelist[i],Nodelist[i+1],w[i]))
vertexlist.append(vertex(Nodelist[3],Nodelist[5],14))
vertexlist.append(vertex(Nodelist[2],Nodelist[5],4))
vertexlist.append(vertex(Nodelist[1],Nodelist[7],11))
vertexlist.append(vertex(Nodelist[2],Nodelist[8],2))
vertexlist.append(vertex(Nodelist[6],Nodelist[8],6))
result=kruskal(Nodesets,vertexlist)
print('end')
    