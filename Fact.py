num = int(input("number: "))
factorial = 1
if num < 0 :
   print("enter a positive number")
elif num==0 :
   print("factorial = 1")
else :
    for i in range(1,num+1):
     factorial*= i
    print(factorial)
    #Alternative
n=int(input(" "))
def factorial(n):
  return 1 if (n==1 or n==0) else n * factorial(n - 1);
print(factorial(n),end="")
# Factorial series
n= int(input("enter a number till you want a series :"))
def Factorial(n):
 if n < 0:
   print("Incorrect input enter a positive number")
 elif n == 0 or n == 1:
   return 1
 else:
   for j in range(n+1):
     return n*Factorial(n-1)
for i in range(n+1):
  print(Factorial(i),end=" ") 
print( "\nanswer term is:",Factorial(n))
