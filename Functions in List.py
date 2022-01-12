fruits=['1','2','3','4','apple','cherry']
print(fruits)
a=fruits.copy();#used to copy that list 
print('second copy')
print(a)
fruits.extend(a)#concatenates also and used to add values at the end 
print(fruits)
x=fruits.count('apple')#count occuring of that value
print(x)
i=fruits.index('cherry')#print the index value of stated value 
print(i)
a.insert(2,"banana")#inserting values at the specific index
print(a)
a.reverse()#reversing  the array
print(a)
print('normal sorting')
a.sort()#normal sorting "ascending"
print(a)
print('reverse sorting')
a.sort(reverse=True)#reverse sorting "descending"
print(a)
print(a[0:3])#print the range of the list user want 
c=a+fruits#concatenation using third variable 
print(c)
