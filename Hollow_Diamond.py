#square with diamond cut out
n=int(input("enter no. of rows "))
for i in range(n,0,-1):
  for j in range(i,0,-1):
    print("*",end=" ")
  for j in range(2*(n-i)):
    print(" ",end=" ")
  for j in range(i,0,-1):
    print("*",end=" ")
  print( )
for i in range(1,n):
  for j in range(i+1):
    print("*",end=" ")
  for j in range(2*(n-i-1)):
    print(" ",end=" ")
  for j in range(i+1):
    print("*",end=" ")
  print( )
  
  #uniquely hollow diamond
  #diamond star pattern 
for i in range(5):
  for j in range(5):
    if i+j==2 or  i-j==2 or  i+j ==6 or j-i==2:
      print("😂",end="")
    else:
     print(end=" ")
  print()
