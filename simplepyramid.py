# SIMPLE PYRAMID 
def pattern(n):
 # k=n 
  for i in range (0,n): 
    for j in range (0,n-i-1): # loop for spacing
      print(end=" ")
   # k=k-1 
    for o in range (0,i+1): # loop for character
      print("😂",end="")
    print("\r")
pattern(2)

# input by user
n=int(input("enter the no of rows you wants print "))
 # k=n 
  for i in range (0,n): 
    for j in range (0,n-i-1): # loop for spacing
      print(end=" ")
   # k=k-1 
    for o in range (0,i+1): # loop for character
      print("😂",end="")
    print("\r")
