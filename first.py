

def compareString(substr, leng):
    global string
    global marker
    global file
    
    start = 0
    end = leng

    cnt = 0

    #starting and ending positions of first site of substr
    memstart = 0
    memend = 0
    
    while True:
        testsubstr = string[start:end]
        #print('test: ',testsubstr, ' ', start, ' ', end)
         
        if(end>len(string)):
            break

        if(testsubstr == substr):
            cnt = cnt+1

            aa = string[0:start]
            bb = string[end:]
            #print("bb: ",bb)
            string = aa + bb
 
            if(cnt == 1):
                memstart = start
                memend = end

        else:
            start += 1
            end += 1

        #print('string: ', string)

        
            
    if(cnt > 1):
        #string = string.replace(substr,'')
        marker = 1
        #print(cnt,' ',substr)
        ss = str(cnt) + ' ' + str(substr)+'\n'
        file.write(ss)
        #print(ss)

    elif(cnt==1):
        string = string[0:memstart] + substr + string[memend:]

    #print('remaining string: ', string)

    

############################

    
def getSubstring(leng=16):
    global string
    global marker
    
    start = 0
    end = leng


    while True:   
        substr = string[start:end]
        #print('substring is: ',substr)
        if(len(string)<leng):
            break
        
        marker = 0
        
        prevstring = string
        compareString(substr, leng)

        if(marker == 0):
            start += 1
            end += 1

            if(start > len(string)):
                break
            continue
            
        #if(prevstring == string):
             #break

        
            
############################



filename = 'sequence2.txt'
string = ''
prevstring = ''
strlength = 0
marker = 0

with open(filename) as f:
    string = f.read().replace('\n','')

string = string.upper()
strlength = len(string)


file = open('output3.txt','a+')

getSubstring(20)

file.close()

print("final string: "+string)











































































