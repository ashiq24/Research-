f = open("bzip_supergene.txt")
s=f.read()
s=s.split('\n')
print(len(s))
map1={}
for i in s:
	#print(i)
	j=i.split()
	#print(j)
	if not j[0] in map1.keys():
		map1[j[0]]=int(j[1])
	else :
		print('error')

f = open('OurMethodCompression.txt')
names=[]
ss=f.read().split('\n')
print(len(ss))
c=[]
c1=[]
for i in ss:
	j=i.split()
	if j[0] in map1.keys():
		names.append(j[0])
		c.append(int(j[1]))
		c1.append(map1[j[0]])

import numpy as np
import matplotlib.pyplot as plt

print(len(c), len(c1), len(names))
#print(c[60],c1[60],names[60])

n_groups = len(c)
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.5
opacity = 1
result = []
avg=0
for i in range(len(c)):
	avg+=(c1[i]-c[i])/c1[i]
	result.append( (c1[i]-c[i])/c1[i] )
	if (c1[i]-c[i])/c1[i] < 0:
		print(names[i])

dummy = range(n_groups)
plt.bar(dummy,result,bar_width,color='b')
#plt.scatter( result,c)
'''rects1 = plt.bar(index, result, bar_width,
                 alpha=opacity,
                 color='r',
                 label='our ')'''
 
print(avg/n_groups)
'''rects2 = plt.bar(index + bar_width, c1, bar_width,
                 alpha=opacity,
                 color='b',
                 label='zip2')'''

#plt.xticks(index + bar_width, )
#plt.legend()
 
#plt.tight_layout()
plt.show()