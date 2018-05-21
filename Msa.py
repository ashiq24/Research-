import Dmst
BITSINNUM=12
THRESHOLD = 50
def loadData(fileName):
    f = open(fileName, 'r')
    data = f.read().split(">")
    Data = []
    for i in data[1:]:
        i=i.split("\n")
        s=[]
        s+=i[1:]
        Data.append(str(s))
        
    return len(Data), Data


def getDiff(r, t):
    Map = {}
    j=-1
    for i in range(len(r)):
        if i<=j:
            continue
        if r[i] != t[i]:
            j = i
            while i < len(r) and r[i] != t[i]:
                i += 1
            subs = t[j:i]
            j=i
            if subs in Map.keys():
                Map[subs] += 1
            else:
                Map[subs] = 1
    cost = 0
    for j in Map.keys():
       # print(j)
        cost += len(j) * 3 + (Map[j]+1) * BITSINNUM
    return cost

def getReduceVal(s):
    cost=0
    count=0
    for c in s:
        if c!='-':
            if count>=5:
                count=0
                cost+=BITSINNUM
            cost+=3
        else:
            count+=1
    if count>=5:
        count=0
        cost+=BITSINNUM+6
    else:
        cost+=count*3
    return cost


def getmatrix(data, num):
    mat = [[0 for i in range(num)] for j in range(num)]
    for i in range(num):
        for j in range(num):
            if i != j:
                mat[i][j] = getDiff(data[i], data[j])
    return mat


def compressData(fileName):
    num, Data = loadData(fileName)
    #Data=Data[:10]
    #num=10
    print(Data[0:2])
    print(num)
    totla_mem=len(Data[0])*3*len(Data)
    print("Total memory "+ str(totla_mem))
    #getDiff('abcdabcdabcdb','aaaaabcdaaaaa')
    weights = getmatrix(Data,num) # this weights is the cost martrix 
    own = []
    for d in Data:
        own.append(getReduceVal(d))
    Edges = []
    for i in range(num):
        for j in range(num):
            if(i==j):
                Edges.append((0,i+1,own[i],0,i+1))
            else:
                Edges.append((i+1,j+1,weights[i][j],i+1,j+1))
    New_mem, refmap =Dmst.dmst(num+1,Edges,0)
    print(New_mem)
    print(New_mem/totla_mem)
    for i in refmap:
        print(i[0]," -> ", i[1])


if __name__ == "__main__":
    '''
    i have corrected the code . Please call this function for every file in a dir .
    and save that result in a file.better if we plot that in a graph by pyplot .
    Python have some in built funtion to get all files in a dir 
    we need create a for loop here 
    that all 
    '''
    compressData("BB30005.tfa_mafft")

    


