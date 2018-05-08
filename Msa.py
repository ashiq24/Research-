def loadData(fileName):
    f = open(fileName, 'r')
    data = f.read().split("\n")
    for i in data:
        if len(i) < 10:
            data.remove(i)
    return len(data), data


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
        cost += len(j) * 3 + Map[j] * 12
    return cost


def getmatrix(data, num):
    mat = [[0 for i in range(num)] for j in range(num)]
    for i in range(num):
        for j in range(num):
            if i != j:
                mat[i][j] = getDiff(data[i], data[j])
    return mat


if __name__ == "__main__":
    num, Data = loadData("input.fasta_muscle")
    print(num)
    print(len(Data[0])*3)
    #getDiff('abcdabcdabcdb','aaaaabcdaaaaa')
    weights = getmatrix(Data,num) # this weights is the cost martrix 
    for i in weights:
        print(i)


