# inverse pyramid pattern 
def pattern(n):
  k=n
  for i in range(n,-1,-1):
    for j in range(k,0,-1):
      print(end=" ")
    k=k+1
    for o in range (0,i+1): # loop for character
      print("😂",end="")
    print("\r")
pattern(2)
