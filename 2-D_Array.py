T = [[11, 12, 5, 2], [15, 6,10,0], [10, 8, 12, 5], [12,15,8,6]]
for r in T:
    for c in r:
        print(c,end = " ")
    print()
    
    # Using above first method to create a 2D array 
rows, cols = (5, 5) 
arr = [[0]*cols]*rows 
print(arr) 
print('')
from numpy import * 
a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
m = reshape(a,(7,5))
print(m)
print("")
# Print data for Wednesday
print(m[2])
print("")
# Print data for friday evening
print(m[4][3])
print("")
#adding a row 
m_r = append(m,[['Avg',12,15,13,11]],0)
print(m_r)
print("")
#Adding a coloumn
m_c = insert(m,[5],[[1],[2],[3],[4],[5],[6],[7]],1)
print(m_c)
print("")
#slicing of an array
m[:,2:4]
print("")
#deleting a row 
m_r = delete(m_r,[7],0)
print(m_r)
print("")
#deleting a coloumn
m_c = delete(m_c,s_[5],1)
print(m_c)
print("")
#updating a row 
m[3] = ['Thu',0,0,0,0]
print(m)
print("")
#updating an element of user choice 
m[1][2]= str(input('t'))
print(m)
print('')
for x in m:
    for y in x:
        print(y,end = " ")
    print()
print("")
#slicing of an array
i= "Mitashi"
print(i)
u=len(i)
print(u)
i[-7:5]
