import numpy as np

import array as arr

c = np.array([1,2,3,4,5,6,7,8,9,10])
a = np.array([1,2,3,4,5])
f = np.array([4, 2, -1, 1])
# print(a[0])
# print(len(a))

# z = np.sort(a)
# print(z)
# #for b in range (0,len(a)):
# for b in z:
#     if z[b]<b:
#         print(z[b],'is less than =',b)
#     else:
#         print(z[b])



if 0 not in a:
    a = np.append(a,0)

print(a)
z=np.sort(a)
print(z)
#for i in range(0,len(z)):
 #   print(z[i],i)
#for j in z:
for i in range(0,len(z)):

    if c[i] in z:
        #print(i)
        if i not in z:
            print("Printing the element that is not in the array z =",i)
        
    else:
        print("Printing the element of array C that is not in array Z  = ",c[i])
        #print("printing I = ",i)
        #if i not in z:
         #   print(i)
        #else:q
         #   print("")
    #else:
     #   print(z[i],c[i])
    
