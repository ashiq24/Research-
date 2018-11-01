# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 07:06:38 2018

@author: User
"""

import math
PER_CHARACTER_BIT=0
MAP_FOR_SYMBOL={}
MAP_FOR_REFERENCE_INDEX={}
current_index=0
MAP_FOR_SYMBOL2={}
PER_CHARACTER_BIT2=0
total_koyta_sequence=0
non_ref=0
ref_=0
highest_index=0
highest_index2=0
reference_list=[]
non_reference_list=[]
final_list=[]
non_ref_dict={}
class non_reference_class:
        indexes=[]
        strings=[]
        reference_number=0
        non_reference_number=0
        is_valid=0
        def __init__(self,reference_number,non_reference_number):
            self.reference_number=reference_number
            self.non_reference_number=non_reference_number
        def add_strings(self,string):
            self.strings.append(string)
        def add_indexes(self,index):
            self.indexes.append(index)
        
class reference_class:
        strings=""
        sequence_number=0
        def __init__(self, sequence_number,strings):
            self.sequence_number = sequence_number
            self.strings = strings
def give_a_tri_get_a_simble(a):
    return MAP_FOR_SYMBOL[a]

def convert_tri_to_string(p):
    return MAP_FOR_SYMBOL2[p]

    
def find_data_until_hash(a,current_index):
    final_data=''
    con=''
    global PER_CHARACTER_BIT
    for i in a[current_index:]:
        con+=i
        if(len(con)==PER_CHARACTER_BIT):
            con=give_a_tri_get_a_simble(con)
            if(con=='#'):
               break
            final_data+=con
            con=''
        current_index+=1
    return final_data,current_index+1
def destuff_data(a,current_index):
    consecutive_one=0
    destuffed_data=''
    j=current_index
    for i in a[current_index:]:
        if consecutive_one==6:
            s=len(destuffed_data)
            return destuffed_data[:s-7],j+1
        if i=='0':
            if consecutive_one==5:
                consecutive_one=0
            else:
                destuffed_data+='0'
                consecutive_one=0
        if i=='1':
            consecutive_one+=1
            destuffed_data+='1'
        j+=1

def return_index_from_destuffed_data(data,koybit):
    indexes=[]
    j=0
    
    for i in range(len(data)):
        if i<j:
            continue
        if data[j]=='0':
            j+=1
            indexes.append(int(data[j:j+koybit*2],2))
            j+=koybit*2
        elif data[j]=='1':
            j+=1
            indexes.append(int(data[j:j+koybit],2))
            j+=koybit
    return indexes
            
            
    
def find_index_of_sequence(a,koy_bit,current_index):
    global ff
    s=a[current_index]
    current_index+=1
    if s=='0':
        reference=int(a[current_index:current_index+koy_bit*2],2)
        current_index+=koy_bit*2
    else:
        reference=int(a[current_index:current_index+koy_bit],2)
        current_index+=koy_bit
    s=a[current_index]
    current_index+=1
    if s=='0':
        non_reference=int(a[current_index:current_index+koy_bit*2],2)
        current_index+=koy_bit*2
    else:
        non_reference=int(a[current_index:current_index+koy_bit],2)
        current_index+=koy_bit
    return reference,non_reference,a,current_index
def main_loop(a,sequence_number_indexing,current_index,ekta_datar_moddhe_indexing_er_jonno_koy_bit_lage):
    reference,non_reference,a,current_index=find_index_of_sequence(a,sequence_number_indexing,current_index)
    current_index=loop_around_a_specific_reference_non_reference(reference,non_reference,current_index,ekta_datar_moddhe_indexing_er_jonno_koy_bit_lage,sequence_number_indexing)
    return current_index
    
def loop_around_a_specific_reference_non_reference(reference,non_reference,current_index,ekta_datar_moddhe_indexing_er_jonno_koy_bit_lage,sequence_number_indexing):
    global non_reference_list
    global MAP_FOR_REFERENCE_INDEX
   # global ff
    global highest_index
    A_NON_REFERENCE=non_reference_class(reference,non_reference)
    A_NON_REFERENCE.strings=[]
    A_NON_REFERENCE.indexes=[]
    if(highest_index<non_reference):
        highest_index=non_reference
    #print("reference index",reference,"non_reference_index",non_reference)
    while(1):
        h,current_index=find_data_until_hash(a,current_index)
        if(len(h)==0):
            print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
            non_reference_list.append(A_NON_REFERENCE)
            break
        
        destuffed_data,current_index=destuff_data(a,current_index)
        indexes=return_index_from_destuffed_data(destuffed_data,ekta_datar_moddhe_indexing_er_jonno_koy_bit_lage)
        A_NON_REFERENCE.add_indexes(indexes)
        A_NON_REFERENCE.add_strings(h)
        if a[current_index:current_index+PER_CHARACTER_BIT]==MAP_FOR_SYMBOL['#']:
            non_reference_list.append(A_NON_REFERENCE)
            current_index+=PER_CHARACTER_BIT
            break
    return current_index
def decompressData(data,koy_bit):
    global total_koyta_sequence
    global reference_list
    global PER_CHARACTER_BIT2
    indexes = []
    all_strings = []
    global highest_index2
    strs=data.split("\n")
    Name={}
    for p in strs:
        if(p.find(",")==-1):
            ind=p.split("|")
            highest_index2=int(ind[0])
            print("highest index is"+str(highest_index2))
            Name=ind[1:]
            break
        else:
            ind=p.split(",")
            index=int(ind[0])
            string=ind[1]
            indexes.append(index)
            all_strings.append(string)
            reference_list.append(reference_class(index,string))
    return indexes, all_strings,ekta_datar_moddhe_indexing_er_jonno_koy_bit_lage, sequence_number_indexing,Name   
    '''
        index = ''
        string = ''
        if i >= len(data):
            break
        
        if data[i] =='0':
            index = data[i+1:i+1+koy_bit*2]
            i = i+1+koy_bit*2
       
        else:
            index = data[i+1:i+1+koy_bit]
            i = i+1+koy_bit
        if(jj==-1):
            highest_index2=index
            jj=0
            continue
        if(highest_index2==index):
            break
        
        index = int(index, 2)
        print('index: ', index)
        total_koyta_sequence+=1
        while(True):
            substring = ''
            substring = data[i:i+PER_CHARACTER_BIT2]
            i = i+PER_CHARACTER_BIT2
           # print(substring)
            substring = convert_tri_to_string(substring)
            
            if(substring == '#'):
                break
            elif(substring == '$'):
                num = ''
                char = string[len(string)-1]
                while(True):
                    num += data[i:i+4]
                    i = i + 4
                    if(data[i] == '1'):
                        num = int(num, 2)
                        i = i + 1
                        break
                    i = i + 1
                for k in range(num-1):
                    string += char
            else:
                string += str(substring)
        
        indexes.append(index)
        all_strings.append(string)
        reference_list.append(reference_class(index,string))
        
    return indexes, all_strings,ekta_datar_moddhe_indexing_er_jonno_koy_bit_lage, sequence_number_indexing
    '''
def find_ref(a,current_index,koy_bit):
    s=a[current_index]
    current_index+=1
    if s=='0':
        reference=int(a[current_index:current_index+koy_bit*2],2)
        current_index+=koy_bit*2
    else:
        reference=int(a[current_index:current_index+koy_bit],2)
        current_index+=koy_bit
    return reference
def convert__from_ref_to_non_ref(r,t):
    global non_ref_dict
    global final_list
    dict=non_ref_dict[r][t]
    s=final_list[r]
    j=0
    for ii in dict.strings:
        prev=0
        for index in dict.indexes[j]:
            if(prev==0):
                s=s[:index]+str(ii)+s[index+len(ii):]
                prev=index
            else:
                prev+=index
                s=s[:prev]+str(ii)+s[prev+len(ii):]
        j+=1
    final_list[t]=s
    
if __name__ == "__main__":
    #per chaarcater bit for ref,nonref file and per character bit2 for ref file
    #map for symbol 2 for ref
    global PER_CHARACTER_BIT
    global MAP_FOR_SYMBOL
    file=open("fial.txt","r")
    '''
    a=''
    af=file.read()
    for i in af:
        a+=format(i,'08b')
        '''
    a=file.read()
    current_index=0
    file.close()
    different_characters=a[:26]
    DF=3
    for i in different_characters:
        if i=='1':
            DF+=1
    PER_CHARACTER_BIT=math.ceil((math.log2((DF))))#DF
    PER_CHARACTER_BIT2=math.ceil((math.log2((DF+1))))
    
    print(PER_CHARACTER_BIT,different_characters)
    j=0
    k=0
    for i in different_characters:
        if i=='1':
            d=format(j,'0'+str(PER_CHARACTER_BIT)+'b')
            MAP_FOR_SYMBOL[d]=chr(ord('a')+k)
            d=format(j,'0'+str(PER_CHARACTER_BIT2)+'b')
            MAP_FOR_SYMBOL2[d]=chr(ord('a')+k)
            print(d,chr(ord('a')+k))
            j+=1
        k+=1
    d=format(j,'0'+str(PER_CHARACTER_BIT)+'b')
    MAP_FOR_SYMBOL[d]='-'
    MAP_FOR_SYMBOL['-']=d
    d=format(j,'0'+str(PER_CHARACTER_BIT2)+'b')
    MAP_FOR_SYMBOL2[d]='-'
    MAP_FOR_SYMBOL2['-']=d
    print('-',MAP_FOR_SYMBOL2['-'])
    j+=1
    d=format(j,'0'+str(PER_CHARACTER_BIT)+'b')
    MAP_FOR_SYMBOL[d]='#'
    MAP_FOR_SYMBOL['#']=d
    d=format(j,'0'+str(PER_CHARACTER_BIT2)+'b')
    MAP_FOR_SYMBOL2[d]='#'
    MAP_FOR_SYMBOL2['#']=d
    print('#',MAP_FOR_SYMBOL2['#'])
    j+=1
    d=format(j,'0'+str(PER_CHARACTER_BIT2)+'b')
    MAP_FOR_SYMBOL2[d]='$'
    MAP_FOR_SYMBOL2['$']=d
    print('$',MAP_FOR_SYMBOL2['$'])
    j+=1
    d=format(j,'0'+str(PER_CHARACTER_BIT2)+'b')
    MAP_FOR_SYMBOL2[d]='?'
    MAP_FOR_SYMBOL2['?']=d
    print('?',MAP_FOR_SYMBOL2['?'])
    ekta_datar_moddhe_indexing_er_jonno_koy_bit_lage=int(a[26:32+26],2)
    sequence_number_indexing=int(a[32+26:64+26],2)
    current_index=26+64
   
    fileName = 'sifatscompression.txt'
    f = open(fileName, 'r')
    data=''
    data=f.read()
    f.close()
    Name={}
    aa, b,ekta_datar_moddhe_indexing_er_jonno_koy_bit_lage,sequence_number_indexing,Name = decompressData(data,sequence_number_indexing)
    outputFile = 'sifatsdecompression.txt'
    f = open(outputFile, 'w')
    for i in range(len(aa)):
        f.write(str(aa[i])+'\n')
        f.write(b[i]+'\n')
        print("index",aa[i])
        ref_+=1
        MAP_FOR_REFERENCE_INDEX[aa[i]]=b[i]
        if(highest_index<aa[i]):
            highest_index=aa[i]
    f.close()
    global highest_index2
    non_ref_=0
    while current_index<len(a):
        current_index=main_loop(a,sequence_number_indexing,current_index,ekta_datar_moddhe_indexing_er_jonno_koy_bit_lage)
        print("\n\n\n")
        total_koyta_sequence+=1
        non_ref_+=1
        
        if find_ref(a,current_index,sequence_number_indexing)==highest_index2:
            
            break
         
        
    print(total_koyta_sequence,"habijabi")

    ss=""
    print("highest index is",highest_index)
    len__=highest_index+1
    non_ref_dict=[[non_reference_class(0,0) for ii in range(len__)]for j in range(len__) ]
    is_visited=[0 for ii in range(len__)]
    edges=[[]for ii in range(len__)]
    indeg=[0 for ii in range(len__)]
    visited=[0 for ii in range(len__)]
    final_list=["" for i in range(len__)]
    for key in MAP_FOR_REFERENCE_INDEX:
        final_list[key]=MAP_FOR_REFERENCE_INDEX[key]
    for i in non_reference_list:
        k=0
        non_ref_dict[i.reference_number][i.non_reference_number]=i
        non_ref_dict[i.reference_number][i.non_reference_number].is_valid=1
        edges[i.reference_number].append(i.non_reference_number)
        indeg[i.non_reference_number]+=1
  
    c=0
    o=0
    while(c<len__-1):
        for i in range(0,len__):
            if(visited[i]==0 and indeg[i]==0):
                visited[i]=1
                for j in edges[i]:
                    indeg[j]-=1
                    if(indeg[j]==0):
                        convert__from_ref_to_non_ref(i,j)
                        print(i,"------>",j)
                        o+=1
                        
                c+=1
    print(o,"oiynihnyi")
    agsa=open("Decompresskorarporfinaldata.txt",'w')
    for i in range(len__):
        agsa.write(">"+Name[i]+"\n")
        agsa.write(final_list[i]+"\n")
    agsa.close()
