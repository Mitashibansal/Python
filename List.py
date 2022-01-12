sum = 0
a = [4,9,0,0,4]
b = [1,2,3,4]
for x in range(0, len(a)):
    sum = sum + a[x]
# sum all the items in a list.
print("Sum of all elements in given list: ", sum)

a.sort()
#get the largest number from a list.
print("Largest element is:", a[-1])
#get the smallest number from a list.
print("Smallest element is:", a[0])
#multiply  all the items in a list with a number
def multiply(List) :
    ans = 1
    for Y in List:
        ans = ans * Y
    return ans
print(multiply(b))
#python class to find two elements from a list that have sum equal to zero 
class math:
  def findpair(nums):
    for i in range(len(nums)-1):
      for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==0:
          print('pair found',nums[i],nums[j])
        """"else:
          print("pair not found")"""

  nums=[-4,9,0,0,4]
  findpair(nums)

