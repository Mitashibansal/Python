#pascals triangle 
 n=int(input("enter no. of rows "))
 def func(n,b):
   r = 1
   if (b> n - b):
       b = n- b
   for i in range(0,b):
       r = r * (n-i)
       r = r //(i+1)
   return r
   
 for i in range (0, n):
     for j in range(0, i + 1):
       print(func(i,j)," ", end="")
     print()
 
