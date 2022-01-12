b= ('animals','uk','uj','lo','jhg','uk')
print(type(b))
from collections import Counter
c=Counter(b)
print(c)
print(tuple(c.elements()))
print(list(c.elements()))
print(set(c.elements()))
print(c.most_common ())
sub ={ 'uk' :1 , 'uj':1 }
print(c.subtract(sub))
print(c)
