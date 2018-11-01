import matplotlib.pyplot as plt
import numpy as np
import sys
import os
import zipfile 
def recursive_path(mypath): 
    for f in listdir(mypath):
        if isfile(join(mypath, f)):
            #print(mypath,' ', f)
            if(f.find("part")==-1):
                onlyfiles.append(join(mypath,f))
        else:
            recursive_path(join(mypath,f))

def zipcompress(fileName):
    import bz2
    compressionLevel=9
    zip = bz2.compress(open(fileName, 'rb').read(), compressionLevel)
    return sys.getsizeof(zip)       
if __name__ == "__main__":
    

    output_file2 = open('bzip_supergene.txt','w')
    
    mypath = 'pep-unfiltered-alignemtns-original'
    from os import listdir
    from os.path import isfile, join
    onlyfiles = []
    recursive_path(mypath)
    array=[]

 
    #m = compressDataExpectation('MSA/23S.E/input.fasta_clustalo')
    n=0
    for f in onlyfiles: 
        #print(f)
        #m=compressData("MSA/"+f)
        #myfile.write(f+"\n")
        if 'tar' in f :
            continue
        print(n)
        n+=1
        locfile = f
        loczip = f+".zip"
        zip = zipfile.ZipFile(loczip, "w", zipfile.ZIP_DEFLATED)
        zip.write (locfile)
        zip.close()
        m= os.path.getsize(f+'.zip')
        output_file2.write(f + '    ' + str(m) + '\n')
        os.remove(f+'.zip')
        
    
    
    print('DONE')

    output_file2.close()
'''tar = tarfile.open(f+'.tar.gz',"w:gz")
        tar.add(f)
        tar.close()
        m= os.path.getsize(f+'.tar.gz')
        output_file2.write(f + '    ' + str(m) + '\n')
        os.remove(f+'.tar.gz')'''