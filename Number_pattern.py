#number pattern 
# for number pattern specify the range of x and then also specify in rows for loop for icrementation and then use x other than astrick
def pattern(n):
  x=0
  for i in range(1,n+1):
    x=x+1
    for j in range(1, 2*n+1):
        if j>i and j< 2*n+1-i:
            print("  ", end="")
        else:
            print(x, end=" ")
    print()
  x=0
  for i in range(n,0,-1):
    x=x+1
    for j in range(2*n,0,-1):
        if j>i and j< 2*n+1-i:
           print("  ", end="")
        else:
            print(x, end=" ")
    print() 
pattern(7)
# decrement 
def pattern(n): 
  x=n
  for i in range(1,n+1):
    x=x-1
    for j in range(1, 2*n+1):
        if j>i and j< 2*n+1-i:
            print("  ", end="")
        else:
            print(x, end=" ")
    print()
  x=n
  for i in range(n,0,-1):
    x=x-1
    for j in range(2*n,0,-1):
        if j>i and j< 2*n+1-i:
           print("  ", end="")
        else:
            print(x, end=" ")
    print() 
pattern(7)

#diamond cutout
n=int(input("enter no. of rows "))
x=n
for i in range(n,0,-1):
  x=x-1
  for j in range(i,0,-1):
    print(x,end=" ")
  for j in range(2*(n-i)):
    print(" ",end=" ")
  for j in range(i,0,-1):
    print(x,end=" ")
  print( )
for i in range(1,n):
  x=x+1
  for j in range(i+1):
    print(x,end=" ")
  for j in range(2*(n-i-1)):
    print(" ",end=" ")
  for j in range(i+1):
    print(x,end=" ")
  print( )
  #diamond pattern 
def pattern(n):
  x=n
  k=n
  for i in range(0,n):
    x-= 1
    for j in range(0,k):
      print(end=" ")
    k=k-1
    for j in range(0,i+1):
      print(x,end=" ")
    print("\r")
  k=0
  for i in range(n,-1,-1):
    x=x+1
    for j in range(k,0,-1):
      print(end=" ")
    k=k+1
    for o in range (0,i+1): # loop for character
      print(x,end=" ")
    print("\r")
pattern(2)
# can be used in columns also 
def pattern(n):
  x=0
  k=n
  for i in range(0,n):
    for j in range(0,k):
      print(end=" ")
    k=k-1
    for j in range(0,i+1):
      x=x+1
      print(x,end=" ")
    print("\r")
  k=0
  for i in range(n,-1,-1):
    for j in range(k,0,-1):
      print(end=" ")
    k=k+1
    for o in range (0,i+1): # loop for character
      x=x+1
      print(x,end=" ")
    print("\r")
pattern(2)
#right pattern 
def pattern(n):
  x=-1
  for i in range (0,n):
    for i in range(0,i+1):
      x= x+1
      print(x,end=" ")
    print("\r")
  for i in range (n,-1,-1):
    for i in range(0,i+1):
      x=x+1
      print(x,end=" ")
    print("\r") 
pattern(3)

def pattern(y):
  n=chr(y)
  for i in range(y,0,-1):
    for j in range(1,i+1):
      print(j, end=" ")
    print("\r")
pattern(6)
  
