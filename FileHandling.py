count = 0
Count = 0
file = open('/content/sample_data/File.txt','r+')
read = file.read()
words = read.split()
'''
for word in words:
  count+=1
print("total words",count) 

lines = read.split("\n")
for i in lines:
  if i:
    Count += 1
print("total lines",Count) 
'''
print("total words",len(words))
num_lines = sum(1 for line in open('/content/sample_data/File.txt'))
print("total lines",num_lines)
