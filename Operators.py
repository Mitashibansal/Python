a= int(input("enter the value of a "))
print(a)
b= int(input("enter the value of b "))
print(b)
print("arithmetic operators")
print(a+b,a-b)
print("assignment operators")
a += 10
print(a)
print("comparision operators")
print(a==b,a>=b,a<=b,a>b,a<b)
print("logical operators")
print(a>b and a<b)
print(a>b or a<b)
print("Identity operators")
list1 =[10,20,30]
list2 =[10,20,30]
x=list1
x is list1
list is list2
list1 is not list2
