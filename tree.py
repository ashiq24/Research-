import numpy as np
from scipy.stats import entropy
import random
class node():
    def __init__(self,boolean):
        self.isleaf = boolean
        self.decission = 0
        self.child = {}
        self.attribute = 0
def classify(data,node):
    if node.isleaf == True:
        return node.decission
    else:
        #print('down')
        #print('node len', len(node.child) , data[ node.attribute ], node.attribute)
        if data[ node.attribute ] not in node.child:
            print("new problem")
            return random.randint(0,1)
        return classify(data,node.child[ data[ node.attribute ] ])
def print_tree(node):
    if node.isleaf == True:
        print('dec ', node.decission)
    else:
        print(node.attribute, 'len ', len(node.child))
        print('----->')
        for  i in node.child.values():
            print_tree(i)
        print('<-----')
    
          
def PLURALITY_VALUE(data):
    print("TAKING PLURARITY")
    n = node(True)
    value,counts = np.unique([i[-1] for i in data], return_counts=True)
    a = np.argmax(counts)
    n.decission = value[a]
    return n

def ent(labels, base=None):
    if len(labels)==0:
        return 0
    value,counts = np.unique(labels, return_counts=True)
    return entropy(counts, base=base)
def importance(data,attr):
    entropies = []
    last = len(data[0])-1
    for i in attr:
        #print(i)
        ua = set( [ l[i] for l in data] )
        e = 0
        for j in ua:
            array = [k[last] for k in data if k[i]==j]
            e = e + len(array)/len(data)*ent(array)
        entropies.append(e)
    a = np.argmin(entropies)
    return attr[a]



def build_tree(data, attr, pdata, alldata, depth):
    if len(data)==0 :
        return PLURALITY_VALUE(pdata)
    elif len(set( [i[-1] for i in data ] ))==1:
        #print("here")
        n = node(True)
        n.decission = data[0][-1]
        return n
    elif len(attr)==0 or depth==0:
        #print('end of attr ')
        return PLURALITY_VALUE(data)
    else:
        Node = node(False)
        index = importance(data,attr)
        #print("chosen ", index)
        newattr = attr[:]
        newattr.remove(index)
        Node.attribute = index
        #print('attr len ', len(newattr))
        for i in sorted(set([ l[index] for l in alldata])):
            newdata = [j for j in data if j[index]==i ]
            cnode = build_tree(newdata, newattr, data,alldata,depth-1)
            #Node.child.append(cnode)
            Node.child[i]=cnode
        return Node
'''
data =[
    [0,0,0,2,0,0],
    [1,1,1,0,0,0],
    [1,0,0,0,0,1],
    [0,2,1,2,0,1],
    [1,1,0,1,0,0],
    [1,1,0,1,1,1],
    [0,0,1,0,0,1],
    [0,1,1,2,1,0],
    [0,2,1,2,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,0],
]
a = [i for i in range(5)]
tree = build_tree(data,a,data,data,0)
print_tree(tree)
for i in data:
    print(classify(i,tree))

'''