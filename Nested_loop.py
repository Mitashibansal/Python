travelling= input('yes or no ')
while travelling =='yes':
  num=int(input('no. of people tavelling '))
  for num in range(1,num +1):
   n= input('name ')
   a= input('age ')
   s= input('sex ')
   print(n)
   print(a)
   print(s)
   break
travelling= input('oops! miss some one ')
