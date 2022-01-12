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
