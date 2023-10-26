import numpy as np

def sort_array(a1):
    for i in range(0,len(a1)):
        for j in range (i+1, len(a1)):
            if(a1[i]>a1[j]):
                temp = a1[j]
                a1[j] = a1[i]
                a1[i]= temp

    return a1
    
a1 = np.array([12,10,34,23,51,31])
print('before sort our array elements is:',a1)
print('After sort our array elements is:',sort_array(a1))


