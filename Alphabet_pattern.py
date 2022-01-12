# alphabetic programs 
"""for alphabetic programs we define characteric limit and then change its value to character by chr() function .
and after that we print that bchanged changed character in this print statement"""
#right pattern 
def pattern(n):
  x=65
  for i in range (0,n):
    for i in range(0,i+1):
      ch=chr(x)
      print(ch,end=" ")
      x= x+1
    print("\r")
  for i in range (n,-1,-1):
    for i in range(0,i+1):
      ch=chr(x)
      print(ch,end=" ")
      x=x+1
    print("\r") 
pattern(4)

#right pattern 
def pattern(n):
  x=64
  for i in range (0,n):
    x= x+1
    for i in range(0,i+1):
      ch=chr(x)
      print(ch,end=" ")
      
    print("\r")
  for i in range (n,-1,-1):
    x= x+1
    for i in range(0,i+1):
      ch=chr(x)
      print(ch,end=" ")
      
    print("\r") 
pattern(4)
#Diamond
def pattern(n):
  y=65
  k=n
  for i in range(0,n):
    for j in range(0,k):
      print(end=" ")
    k=k-1
    for j in range(0,i+1):
      x=chr(y)
      print(x, end=" ")
      y=y+1
    print("\r")
  k=0
  for i in range(n,-1,-1):
    for j in range(k,0,-1):
      print(end=" ")
    k=k+1
    for o in range (0,i+1): # loop for character
      x=chr(y)
      print(x, end=" ")
      y=y+1
    print("\r")

pattern(26)
# pyramid
def pattern(n):
  x=65
  k=n 
  for i in range (0,n): 
    y=chr(x)
    x=x+1
    for j in range (0,k): # loop for spacing
      print(end=" ")
    k=k-1 
    for o in range (0,i+1): # loop for character
      print(y,end=" ")
    print("\r")
pattern(26)
#right star pattern 
def pattern(n):
  x=65
  for i in range (0,n):
    y=chr(x)
    x=x+1
    for i in range(0,i+1):
      print(y,end=" ")
    print("\r")
  for i in range (n,-1,-1):
    y=chr(x)
    x=x+1
    for i in range(0,i+1):
      print(y,end=" ")
    print("\r") 
pattern(3)

