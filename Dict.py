from collections import OrderedDict
d= OrderedDict()
d[2]=0
d[1]=9
d[4]=10
d[3]=99
print(d)
print(d.keys())
print(d.items())
d[1]=8
a= dict(d)
print(a)
a[1]= 9
print(a.values())

from collections import defaultdict

d= defaultdict(set)
d['1']= 'p'
d['2']= 'i'
print(d[0])
