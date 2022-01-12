#create a set.
s1={1,2,3,4}
print(s1)
#add member(s) in a set.
s1.add('mita')
print(s1)
#remove item(s) from set
s1.discard('mita')
print(s1)
#remove an item from a set if it is present in the set.
s1.remove(4)
print(s1)
for i in range(int(input())):
    a = int(input());
    A = set(input().split()) 
    b = int(input()); 
    B = set(input().split())
    print(A.issubset(B))
    
s = set(input().split())
ans = True
for i in range(int(input())):
    t = set(input().split())
    if (s > t) == False:
        ans = False
        break
print(ans)
