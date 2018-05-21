
Result = []

def addEdge(e):
    #print('addedge ', e)
    for i in Result:
        if(i[4] == e[4]):
            Result.remove(i)

    Result.append(e)


def dmst(vertices, test, root=0):
    oo = int(1e9)
    #print(test)
    cost = {}
    back = {}
    label = {}
    bio = {}
    edge = {}

    ret = 0
    while(True):
        for i in range(vertices):
            cost[i] = oo

        for e in test:
            if(e[0] == e[1]):
                continue
            if(e[2] < cost[e[1]]):
                #print("found", e[1])
                cost[e[1]] = e[2]
                back[e[1]] = e[0]
                edge[e[1]] = e

        cost[root] = 0

        for i in range(vertices):
            if(cost[i] == oo):
                print('problem at ', i)
                return -1


        for i in range(vertices):
            ret += cost[i]
            if(i!=root):
                addEdge(edge[i])

        K = 0
        for i in range(vertices):
            label[i] = -1
            bio[i] = -1

        for i in range(vertices):
            x = i
            while(True):
                if(x != root and bio[x] == -1):
                    bio[x] = i
                    x = back[x]
                else:
                    break

            if(x != root and bio[x] == i):
                while(True):
                    if(label[x] == -1):
                        label[x] = K
                        x = back[x]
                    else:
                        break
                K = K + 1

        #print('oikhane')
        if(K==0):
            break

        for i in range(vertices):
            if(label[i] == -1):
                label[i] = K
                K = K + 1


        for e in range(len(test)):
            xx = label[test[e][0]]
            yy = label[test[e][1]]
            if(xx != yy):
                zz = test[e][2] - cost[test[e][1]]
                test[e] = (test[e][0],test[e][1], zz, test[e][3],test[e][4])

            test[e] = (xx, test[e][1],test[e][2],test[e][3],test[e][4])
            test[e] = (test[e][0], yy, test[e][2],test[e][3],test[e][4])


        root = label[root]
        vertices = K
    
    result= Result[:]
    Result.clear()
    return ret, result

'''
to input to this code, first enter number of edges and vertices
in terminal and write the values of u, v, w in a file(just to make
the input process faster)


sample input
4 6
0 1 6
0 3 4
1 3 3
2 1 2
2 0 1
3 2 5

another input
6 9
0 1 1
1 2 1
2 0 1
5 3 1
3 4 1
4 5 1
1 5 3
2 5 4
0 4 5


'''







































