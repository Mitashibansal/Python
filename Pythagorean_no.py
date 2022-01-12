from math import sqrt
n =int(input('Maximum number (no. must be greater than 4) '))
for a in range (1,n+1):
  for b in range (a,n):
    c_square=a**2 + b**2
    c= int(sqrt(c_square))
    if ((c_square - c**2)==0) & (c<=n):
      print(a,b,c)
 # using map
side = list(map(int,input().split()))
x,y,z = sorted(side)
if x**2+y**2==z**2:
  print("YES",end="")
else:
  print("NO",end="")
      
