import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np
from scipy.stats import entropy
from sklearn import preprocessing
import tree
def ent(labels, base=None):
    if len(labels)==0:
        return 0
    value,counts = np.unique(labels, return_counts=True)
    return entropy(counts, base=base)
def get_thresold(ary,terget):
    tup = []
    for i in range(len(ary)):
        tup.append( (ary[i],terget[i]) )
    tup.sort(key=lambda x:x[0])
    entropies = []
    value,counts = np.unique(terget, return_counts=True)
    entropies.append(entropy(counts,None))
    ly,ln,ry,rn = 0.0,0.0,1.0*counts[0],1.0*counts[1]
    for i in range(len(tup)):
        if tup[i][1]==value[0]:
            ly+=1
            ry-=1
        else:
            ln+=1
            rn-=1
        #print(ly,ln,ry,rn)
        if ry==0 and rn==0:
            e = (ly+ln)/len(ary)*entropy([ly,ln],None)
        else:
            e = (ly+ln)/len(ary)*entropy([ly,ln],None)+(ry+rn)/len(ary)*entropy([ry,rn],None)
        entropies.append(e)
    #print(entropies)
    a = np.argmin(entropies)
    if a==0:
        return tup[a][0]-1
    elif a==len(ary):
        return tup[-1][0]+1
    else :
        return (tup[a-1][0]+tup[a][0])/2

    
print('test ', get_thresold([10,11,12,1,2,3],[1,1,1,0,0,0]))

#print(c)
def dataclean():
    file = open('adult_data.txt')
    data = file.read().split('\n')
    data = [i.split(',') for i in data]
    print(len(data[0]))
    condata = [ [ i[0],i[2],i[4],i[10],i[11],i[12] ] for i in data]

    catdata = [ [i[1],i[3],i[9],i[5],i[6],i[7],i[8],i[13] ] for i in data ]
    catdata = [ [j.strip() for j in i ] for i in catdata ]
    label = [ i[-1] for i in data]
    ##############################################
    s = list(set(label))
    s.sort()
    #s.reverse()
    label = [s.index(i) for i in label]
    print(label[:10])

    con = pd.DataFrame(condata)
    cat = pd.DataFrame(catdata,dtype="category")

    con = con.apply(pd.to_numeric, errors='coerce')
    print(con.describe())
    print(con.head())
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    imp.fit(con)
    con = imp.transform(con)

    #print(cat.describe())
    #print(cat.groupby(0).size())

    imp2 = SimpleImputer(missing_values='?',strategy="most_frequent")
    cat = imp2.fit_transform(cat)
    cat = pd.DataFrame(cat)
    #print(cat.groupby(0).size())
    encode = preprocessing.OrdinalEncoder()
    encode.fit(cat)

    cat = encode.transform(cat)

    #print(cat[90:100])
    #print(con[:10])
    for i in range(len(con[0])):
        print(i)
        arr = [ j[i] for j in con ]
        tval = get_thresold(arr,label)
        for j in range(len(con)):
            if con[j][i]< tval:
                con[j][i] = 0
            else:
                con[j][i] =1
    print(con[:10])
    print(cat[:10])
    #label = np.array(label,ndmin=2)
    data = np.concatenate((con,cat), axis = 1).tolist()
    for i in range(len(data)):
        data[i].append(label[i])
    print(data[:4])
    attr = [i for i in range(len(data[0])-1)]
    return data, attr
def dataclean2():
    data = pd.read_csv("WA_Churn.csv")
    data[data.Churn.notna() ]
    print(len(data['Churn']))
    label = data['Churn']
    #print(label[:3])
    concol =[]
    catcol = []
    for i in data.columns:
        if i!='Churn' and i!='customerID':
            print(i)
            s = data[i]
            if len(set(s))<=10:
                catcol.append(i)
            else:
                concol.append(i)
    condata = data[concol]
    catdata = data[catcol]
    for i in catcol:
        #print('NULL VALUE',catdata[i].isnull().sum())
        catdata[i]=catdata[i].astype('category')
    s = list(set(label))
    s.sort()
    #s.reverse()
    label = [s.index(i) for i in label]
    #print(label[:10])

    con = condata
    cat = catdata

    for i in catcol:
        print(cat.groupby(i).size())
    for i in concol:
        print(con.groupby(i).size())
    #print(con.head())
    #print(cat.head())

    con = con.apply(pd.to_numeric, errors='coerce')
    #print(con.describe())
    #print(con.head())
   
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    imp.fit(con)
    con = imp.transform(con)
    
    #print(cat.describe())
    
    imp2 = SimpleImputer(strategy="most_frequent")
    cat = imp2.fit_transform(cat)
    cat = pd.DataFrame(cat)
    #print(cat.groupby(0).size())

    encode = preprocessing.OrdinalEncoder()
    encode.fit(cat)

    cat = encode.transform(cat)

    #print(cat[90:100])
    #print(con[:10])
    for i in range(len(con[0])):
        print(i)
        arr = [ j[i] for j in con ]
        tval = get_thresold(arr,label)
        for j in range(len(con)):
            if con[j][i]< tval:
                con[j][i] = 0
            else:
                con[j][i] =1
    print(con[:10])
    print(cat[:10])
    #label = np.array(label,ndmin=2)
    data = np.concatenate((con,cat), axis = 1).tolist()
    for i in range(len(data)):
        data[i].append(label[i])
    print(data[:4])
    attr = [i for i in range(len(data[0])-1)]
    return data, attr

        
data, attr = dataclean2()
#data, attr = dataclean()
#node = tree.build_tree(data,attr,data,data,6)
#tree.print_tree(node)
hypos, W = tree.adaboost(data,20)
c,w=0,0
p, n =0,0
for i in data:
    res = tree.adaclassify(hypos,W,i)
    #print(res)
    if res==i[-1]:
        c+=1
        
    else:
        w+=1
        print("true ",i[-1],' false ',res)
print(c/(c+w))