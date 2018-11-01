# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 07:05:54 2018

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 00:58:11 2018

@author: User
"""
import math
from bitstring import  BitArray
#MAP_FOR_SYMBOL={}
MAP_FOR_SYMBOL2={} 
final_final_string=''#
final_bit=bytearray()
final_bit2=bytearray()
final_final_string2=''
#fff=open("kik2.txt",'w')#
def give_a_string_put_in_byte_array2(d):
    global final_bit2
    h=BitArray(bin=d)
    h=h.tobytes()
    for i in h:
        final_bit2.append(i)
def give_a_string_put_in_byte_array(d):
    global final_bit
    h=BitArray(bin=d)
    h=h.tobytes()
    for i in h:
        final_bit.append(i)

def convert_string_to_tri2(p):
    return MAP_FOR_SYMBOL2[p]
def get_xored(data):
    a=0
    for i in data:
        for j in i:
            a|=int(math.pow(2,int(ord(j)-ord('a'))))
    return a
'''
def putInCompressionFile(index,koy_number_data_index, data_index, string):
    #print('www: ',data_index)
    result = ''
    
    result+= get_binary_in_file(index,koy_number_data_index)#,file)
    i=0
    while(True):
        if(i >= len(string)):
           break
        if(i==(len(string)-1) and string[i]>='0' and string[i]<='9'):
            break
        
        if(string[i]=='$'):
            result += MAP_FOR_SYMBOL['$']
            j = i+1
            num = ''
            for j in range(i+1, len(string), 1):
                if(string[j]>='0' and string[j]<='9'):
                    num += string[j]
                else:
                    break
            i = j-1
            num = int(num)
            num = dec_to_bin(num)
            num = fixLengthToMultipleOfFour(len(str(num)), num)
            result += num
        else:
            result += convert_string_to_tri(string[i])

        i = i+1
        

    result +=MAP_FOR_SYMBOL['#']
    #print('res: ', result)
    return result
    '''
def compressString(string):
    #print('len: ', len(string), ' str: ', string)
    compressed = ''
    i = 0
    while(True):
        if(i == len(string)-1 and string[len(string)-1]!=string[len(string)-2]):
            compressed += string[i]
            break
        elif(i >= len(string)-1):
            break
        
        if(string[i]==string[i+1]):
            compressed += string[i]
            num = 2
            j = i+1
            for j in range(i+1, len(string)-1, 1):
                if(string[j] == string[j+1]):
                    num = num + 1
                else:
                    break
            i=j
            if(num>5):
                compressed += '$' + str(num)
            else:
                for k in range(num-1):
                    compressed += string[i]
        else:
            compressed += string[i]
        i = i+1
        #print('s:',string[i], ' i: ', i)
    return compressed


def dec_to_bin(x):
    return int(bin(x)[2:])

def fixLengthToMultipleOfFour(length, actual_num):
    result = str(actual_num) 
    b = length % 4
    if(b == 1):
        result = '000' + result
    elif(b==2):
        result = '00' + result
    elif(b==3):
        result = '0' + result
 
    i=4
    while(i<len(result)):
        result = result[:i] + '0' + result[i:]
        i = i + 5

    result += '1'

    return result
def get_binary_in_file(ki_likhbo,koy_bit_e_likhbo):
    stri='0'+str(koy_bit_e_likhbo*2)+'b'
    a=format(ki_likhbo,stri)
    j=1
    for i in a[:koy_bit_e_likhbo]:
        if i=='1':
            j=0
            break
    if j==0:#pura sob biti lagbe
        return '0'+a
    else:#half bit enough
        return '1'+a[koy_bit_e_likhbo:]
    
def write_in_binary_in_file(ki_likhbo,koy_bit_e_likhbo,file):
    global final_final_string
    stri='0'+str(koy_bit_e_likhbo*2)+'b'
    a=format(ki_likhbo,stri)
    j=1
    for i in a[:koy_bit_e_likhbo]:
        if i=='1':
            j=0
            break
    if j==0:#pura sob biti lagbe
        final_final_string=final_final_string+'0'+a
       # file.write('0'+a)
    else:#half bit enough
        final_final_string=final_final_string=final_final_string+'1'+a[koy_bit_e_likhbo:]
        #file.write('1'+a[koy_bit_e_likhbo:])
def give_string_in_binary(number,koy_bit):
    stri='0'+str(koy_bit*2)+'b'
    a=format(number,stri)
    j=1
    for i in a[:koy_bit]:
        if i=='1':
            j=0
            break
    if j==0:#pura sob biti lagbe
        return '0'+a[:koy_bit]+a[koy_bit:]
    else:#half bit enough
        return '1'+a[koy_bit:]
def bitstuff(d):
    number_of_consecutive_one=0
    result=''
    for i in d:
        if i=='1':
            result+='1'
            number_of_consecutive_one+=1
            if number_of_consecutive_one==5:
                result+='0'
                number_of_consecutive_one=0
        else:
            result+='0'
            number_of_consecutive_one=0
    return result

def check_mates(dict,r,t,datar_index,koy_number_data_index,file,reference_index,non_reference_index):
    global final_final_string
    write_in_binary_in_file(reference_index,koy_number_data_index,file)
    write_in_binary_in_file(non_reference_index,koy_number_data_index,file)
#    fff.write(str(reference_index)+"-------->"+str(non_reference_index)+"\n")
    #print(reference_index,"-------->",non_reference_index)
    final_string_to_write=''
    d='jj'
    for key in dict:#key holo kon value
        for p in key:
            final_string_to_write+=convert_string_to_tri2(p)
       # fff.write(key+"\t")
        final_string_to_write+=MAP_FOR_SYMBOL2['#']
        d=''
        prev=0
        for j in dict[key].split(','):
            if(prev==0):
                prev=int(j)
                num=prev
            else:
                num=int(j)-prev
                prev=int(j)
           # num=int(j)
      
            d+=give_string_in_binary(num,datar_index)
        d=bitstuff(d)
        final_string_to_write+=d
        final_string_to_write+='01111110'
        #fff.write("\n")
    final_string_to_write+=MAP_FOR_SYMBOL2['#']
    final_final_string+=final_string_to_write
    '''
    u=(int)(len(final_final_string)/8)
    u=math.floor(u)
    print(u*8,'ji')
    if(u>=1):
        give_a_string_put_in_byte_array(final_final_string[:u*8])
        final_final_string=final_final_string[u*8:]
    '''
   # file.write(final_string_to_write)
