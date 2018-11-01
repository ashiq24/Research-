# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 07:06:15 2018

@author: User
"""

import Dmst
import math
import os
import sys
import compression2
import zipfile
BITSINNUM=12
BITSIID = 12
PER_CHARACTER_BIT=0#

PER_CHARACTER_BIT2=0#
MAP_FOR_SYMBOL2={}#

output_file2 = open('OurMethodCompression.txt','w')
from re import sub
 
def encode(text):
    return sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1),
               text)
 
def decode(text):
    '''
    Doctest:
        >>> decode('12W1B12W3B24W1B14W')
        'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
    '''
    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)),
               text)

def recursive_path(mypath): 
    for f in listdir(mypath):
        if isfile(join(mypath, f)):
            #print(mypath,' ', f)
            if(f.find("part")==-1 or f.find("mastcom")==-1):
                onlyfiles.append(join(mypath,f))
        else:
            recursive_path(join(mypath,f))



def loadData(fileName):
    f = open(fileName, 'r')
    data = f.read().split(">")
    Data = []
    Name = []
    a=0#
    ind=0#
    agsa=open("COMPRESSKORARAGEFILE.txt",'w')#
    for i in data[1:]:
        j=i.split("\n")
        s=[]
        Name.append(j[0])
        for k in j[1:]:
            s.extend(k)
        Data.append(''.join(s).strip().lower())
        agsa.write(str(ind)+"\t")
        agsa.write(''.join(s).strip().lower())
        agsa.write("\n")
        ind+=1
    agsa.close()
    a=compression2.get_xored(Data)#
    len_check = [ len(i) for i in Data]
    if min(len_check)!= max(len_check):
    	print("FATAL ERROR > LENGTHS NOT EQUAL ")
    	raise Exception("FATAL ERROR > LENGTHS NOT EQUAL ")

    return len(Data), Data,a,Name#
def getProbability(Data, interval):
    length = len(Data[0])
    probabilities = [dict() for i in range(length)]
    num = len(Data)
    actual_lenth = len(Data[0])
    for i in range(actual_lenth):
        for j in range(len(Data)):
            if i+interval<=len(Data[0]):
                c = Data[j][i:i+interval]
            else :
                c = Data[j][i:] 
            if c in probabilities[i]:
                probabilities[i][c]+=1
            else:
                probabilities[i][c]=1
        for c in probabilities[i]:
            probabilities[i][c]=probabilities[i][c]/num
    return probabilities

def getExpectations(Data,probabilities,interval):
    expectation = []
    for i in Data:
        expec = 0
        #print(i)
        for j in range(len(i)) :
            #print(i[j])
            if j+interval<=len(i):
                c=i[j:j+interval]
            else:
                c=i[j:]
            expec += math.log(probabilities[j][c])
        
        expectation.append(expec)
    return expectation


def getExpectations_2(Data,probabilities,interval):
    l=[]
    distance_2=[]
    
    
    for i in probabilities:
        l.append( max(i,key=i.get))
    
    k=0
    for i in Data:
        #dis=0
        dis2=0
        for j in range(len(i)):
            if( l[j]!=i[j]):
                #dis+=1
                dis2+=1-probabilities[j][i[j]]
        #distance.append(dis)
        distance_2.append(dis2)
        k+=1
    orderedpairs_3 = [ (i,j) for  j,i in enumerate(distance_2) ]
    orderedpairs_3.sort()
    order_3 = [ i for j,i in orderedpairs_3]
    return order_3



def getDiff(r, t):
    Map = {}
    dict={}#
    j=-1
    for i in range(len(r)):
        if i<=j:
            continue
        if r[i] != t[i]:
            j = i
            while i < len(r) and r[i] != t[i] :
                i += 1
                if i<len(r) and r[i]==t[i]:
                    if i+1<len(r) and r[i+1]!=t[i+1]:
                        i+=1
                    elif i+2<len(r) and r[i+2]!=t[i+2]:
                        i+=2
                    elif i+3<len(r) and r[i+3]!=t[i+3]:
                        i+=3
                    elif i+4<len(r) and r[i+4]!=t[i+4]:
                        i+=4
            subs = t[j:i]
            index=j#
            j=i
            if subs in Map.keys():
                Map[subs] += 1
                dict[subs]+=","+str(index)#
            else:
                Map[subs] = 1
                dict[subs]=str(index)#
    cost = 0
    for j in Map.keys():
       # print(j)
        cost += len(j) * 8 + (Map[j]) * (BITSINNUM+5)
    return cost,dict#

def getReduceVal(s):
    global BITSINNUM
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


def getmatrix(Data, num, length, overlap,order1):

    weights=[[-1 for i in range(num)] for j in range(num)]
    dict = [[0 for i in range(num)] for j in range(num)]#
    

    for i in range(0,num-length,length-overlap):
        if(i+length>num):
            m=order1[i:]
            #m2=order2[i:]
        else:
            m=order1[i:i+length]
            #m2=order1[i:i+length]
        for i in m:
            for j in m:
                dict[i][j]={}#
                if(i!=j and weights[i][j]==-1):
                    weights[i][j],dict[i][j]=getDiff(Data[i], Data[j])#
    
    for i in range(num):
        if i!=num-1:
            dict[num-1][i]={}#
            weights[num-1][i],dict[num-1][i]=getDiff(Data[num-1],Data[i])#
    return weights,dict#



def compressDataExpectation(fileName):
    global BITSIID
    global BITSINNUM
    global MAP_FOR_SYMBOL2
    
    Name={}
    num, Data,different_characters,Name = loadData(fileName)#
    different_characters=format(different_characters,'026b')#
    #print("uck",different_characters)#
    foo=num+1#
    global PER_CHARACTER_BIT#
    global PER_CHARACTER_BIT2#
    dict = [[0 for i in range(foo)] for j in range(foo)]#
    DF=4
    #print(num, len(Data[1]))
    BITSINNUM= int( math.log2(len(Data[0])))+1
    BITSIID =  int( math.log2(num))+1
    different_characters=different_characters[::-1]#
    for i in different_characters:#
        if i=='1':#
            DF+=1#
    PER_CHARACTER_BIT=math.ceil((math.log2((DF))))#
    PER_CHARACTER_BIT2=math.ceil((math.log2((DF))))#DF-1
    j=0#
    k=0#
    for i in different_characters:#
        if i=='1':#
            d=format(j,'0'+str(PER_CHARACTER_BIT)+'b')#
            d=format(j,'0'+str(PER_CHARACTER_BIT2)+'b')#
            MAP_FOR_SYMBOL2[chr(ord('a')+k)]=d#
            j+=1#
        k+=1#
    d=format(j,'0'+str(PER_CHARACTER_BIT)+'b')#
    print('-',d)
    #print("n\n\n\n\n"+MAP_FOR_SYMBOL['-']+"\m\n\\n\n\n\n")
    d=format(j,'0'+str(PER_CHARACTER_BIT2)+'b')#
    MAP_FOR_SYMBOL2['-']=d#
    j+=1#
    d=format(j,'0'+str(PER_CHARACTER_BIT)+'b')#
    print('#',d)
    d=format(j,'0'+str(PER_CHARACTER_BIT2)+'b')#
    MAP_FOR_SYMBOL2['#']=d#
    j+=1#
    d=format(j,'0'+str(PER_CHARACTER_BIT)+'b')#
    MAP_FOR_SYMBOL2['$']=d#symbol2 amar
    print('$',d)
    j+=1#
    d=format(j,'0'+str(PER_CHARACTER_BIT)+'b')#
    MAP_FOR_SYMBOL2['?']=d#symbol2 amar
    print('?',d)
    compression2.MAP_FOR_SYMBOL2=MAP_FOR_SYMBOL2
    print("GENE NUMBER ", num)#
    totla_mem=len(Data[0])*3*len(Data)
    #print("Total memory "+ str(totla_mem))
    #getDiff('abcdabcdabcdb','aaaaabcdaaaaa')

    prob = getProbability(Data,1)
    #print(prob)

    order3 = getExpectations_2(Data,prob,1)
    ###################
    own = []
    for d in Data:
        own.append(getReduceVal(d))

    weights1,dict = getmatrix(Data,num,5,3,order3)
    ##########################

    Edges = []
    for i in range(num):
        for j in range(num):
            
            if(i==j):
                Edges.append((0,i+1,own[i],0,i+1))
            elif weights1[i][j]==-1:
                continue
            else:
                Edges.append((i+1,j+1,weights1[i][j],i+1,j+1))
    solution, refmap2 =Dmst.dmst(num+1,Edges,0)
    New_mem2 = solution + +BITSIID*num
    #print("new memory",New_mem2/8)
    #print("--->",New_mem2/totla_mem)
    
    check=0
    import os
    FolderName=fileName+'.mstcom/'
    
    os.makedirs(os.path.dirname(FolderName), exist_ok=True)
    fileName=FolderName+ "sifatscompression.txt"
    fileName2= FolderName+ "fial"

   
    
    file=open(fileName,'w')#
    file2=open(fileName2,'w')#
    file2.seek(0)
    file2.truncate()
    file2.close()
    file.seek(0)
    file.truncate()
    file.close()
    file=open(fileName,'w')#
    file2=open(fileName2,'w')#
    compression2.final_final_string+=different_characters
    #file2.write(different_characters)#
    datar_index=BITSINNUM#
    koy_number_data_index=BITSIID#
    if datar_index%2!=0:#
        datar_index+=1#
    if koy_number_data_index%2!=0:#
        koy_number_data_index+=1#
    datar_index=datar_index/2#
    datar_index=math.ceil(datar_index)#
    koy_number_data_index=koy_number_data_index/2#
    koy_number_data_index=math.ceil(koy_number_data_index)#
    a=format(datar_index,'032b')#
   # file2.write(a)#
    compression2.final_final_string+=a
    a=format(koy_number_data_index,'032b')#
    #file2.write(a)#
    compression2.final_final_string+=a
    '''
    u=(int)(len(compression2.final_final_string)/8)
    u=math.floor(u)
    if(u>=1):
        compression2.give_a_string_put_in_byte_array(compression2.final_final_string[:u*8])
        compression2.final_final_string=compression2.final_final_string[u*8:]
    '''
    k=0#
    bal=0#
    total_ref=0#
    total_non_ref=0#
   # compression2.final_final_string2+=compression2.get_binary_in_file(num,koy_number_data_index)
    for i in refmap2:
        #print( i[0],i[1])
        j=i[0]
        k=i[1]
        bal+=1#
        if(j==0):
            check+=own[k-1]
        else:
            check+=weights1[j-1][k-1]
        if(i[0]==0):
            total_ref+=1
           # print(str(i[1]-1)+','+Data[i[1]-1]+"\n")
            file.write(str(i[1]-1)+','+Data[i[1]-1]+"\n")
        else :
            total_non_ref+=1
            compression2.check_mates(dict[i[0]-1][i[1]-1],Data[i[0]-1],Data[i[1]-1],datar_index,koy_number_data_index,file2,i[0]-1,i[1]-1)#,Data[i[3
            k+=1
    fff=str(num)
    for i in Name:
        fff=fff+"|"+i
    fff+="\n"
    file.write(fff)
    compression2.write_in_binary_in_file(num,koy_number_data_index,file)
    '''
    compression2.give_a_string_put_in_byte_array2(compression2.final_final_string2) 
    compression2.give_a_string_put_in_byte_array(compression2.final_final_string)   
    #file.write(compression2.final_bit2)
    file2.write(compression2.final_bit)
    '''
    file2.write(compression2.final_final_string)
    file2.flush()
    #file2.write(MAP_FOR_SYMBOL2['#'])


    file2.close()
    file.close()

    
    print("ref",total_ref,"non",total_non_ref)
     

    if( check==solution):
        print("now ok ")
    else:
        print("still problem", solution, check)

    '''import bz2
    compressionLevel=9
    tarbz2contents1 = bz2.compress(open(fileName, 'rb').read(), compressionLevel)
    tarbz2contents2 = bz2.compress(open(fileName2, 'rb').read(), compressionLevel)
    import tarfile
    tarname = fileName+'sifatmast.tar.gz'
    tar = tarfile.open(tarname, "w:gz")
    tar.add(fileName)
    tar.close()
    tarname2 = fileName+'fialmast.tar.gz'
    tar = tarfile.open(tarname2, "w:gz")
    tar.add(fileName2)
    tar.close()

    size1 = os.path.getsize(tarname)
    size1+= os.path.getsize(tarname2)
    '''
    locfile = fileName
    loczip = fileName+"sifatmast.zip"
    zip = zipfile.ZipFile(loczip, "w", zipfile.ZIP_DEFLATED)
    zip.write (locfile)
    zip.close()
    size1= os.path.getsize(fileName+'sifatmast.zip')
    
    locfile = fileName2
    loczip = fileName2+"fialmast.zip"
    zip = zipfile.ZipFile(loczip, "w", zipfile.ZIP_DEFLATED)
    zip.write (locfile)
    zip.close()
    size1+= os.path.getsize(fileName2+'fialmast.zip')


    '''file=open(fileName,'wb')#
    file2=open(fileName2,'wb')#
    file2.seek(0)
    file2.truncate()
    file.seek(0)
    file.truncate()

    file.write(tarbz2contents1)
    file2.write(tarbz2contents2)

    file.flush()
    file2.flush()

    file.close()
    file2.close()
 
    #print('filenames are: ', fileName , '   ' , fileName2)
    ff1 = open(fileName)
    ff2 = open(fileName2) 
    size1 = os.path.getsize(fileName)
    size2 = os.path.getsize(fileName2)'''
    #size1 = sys.getsizeof(tarbz2contents1) + sys.getsizeof(tarbz2contents2)
    #print('size: ' + str(size1))
    
    n1 = fileName.split('/')
    name = ''
    for xx in n1:
        if(xx !='sifatscompression.txt'):
            name += xx + '/'

    name = name[:-8]  
    #print('name: ' + name + ' , size: ' + str(size1))
    output_file2.write(name + '    ' + str(size1) + '\n')
    output_file2.flush()
    #ff1.close()
    #ff2.close()
    #os.rmdir(FolderName)
    BITSINNUM=12
    BITSIID = 12
    PER_CHARACTER_BIT=0#
   
    PER_CHARACTER_BIT2=0#
    MAP_FOR_SYMBOL2={}#
   

    compression2.MAP_FOR_SYMBOL2={} 
    compression2.final_final_string=''#
    compression2.final_bit=bytearray()
    compression2.final_bit2=bytearray()
    compression2.final_final_string2='' 
    

if __name__ == "__main__":
    '''
    i have corrected the code . Please call this function for every file in a dir .
    and save that result in a file. better if we plot that in a graph by pyplot .
    Python have some in built funtion to get all files in a dir 
    we need create a for loop here 
    that all 
    '''
   # import sys
    #file = sys.argv[1]
    #compressDataExpectation("input.fasta_muscle")
    #compressDataExpectation("input.fasta_fsa")
    #compression2.fff.close()
    #compressDataExpectation("input.fasta_muscle")
    #compressDataExpectation("true.reduced.fasta")
    
    #compressDataExpectation("true.fasta")
    #compressDataExpectation("input.fasta_fsa")
    #compressDataExpectation("acanthisitta-chloris.fasta")
    import matplotlib.pyplot as plt
    import numpy as np
    
    mypath = 'pep-unfiltered-alignemtns-original'
    from os import listdir
    from os.path import isfile, join
    #onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    onlyfiles = []
    recursive_path(mypath)
    #print(onlyfiles)
    #onlyfiles = onlyfiles[:10]
    array=[]

 
    #m = compressDataExpectation('MSA/23S.E/input.fasta_clustalo')
    n=0
    for f in onlyfiles: 
        if 'tar'in f or 'sifat' in f or 'fial' in f:
            continue
        #m=compressData("MSA/"+f)
        #myfile.write(f+"\n")
        compressDataExpectation(f)
        try:
            m =1
        except:
            continue
        array.append(m)

        n+=1
        print(f+'  file number ', n)

    
    
    print('DONE')

    output_file2.close()
