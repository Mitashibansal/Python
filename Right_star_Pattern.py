#right star pattern 
def pattern(n):
  for i in range (0,n):
    for i in range(0,i+1):
      print("* ",end="")
    print("\r")
  for i in range (n,-1,-1):
    for i in range(0,i+1):
      print("* ",end="")
    print("\r") 
pattern(3)
