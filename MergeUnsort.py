def sortedMerge(a, b, res, n, m): 
     
    i, j, k = 0, 0, 0
    while (i < n): 
        res[k] = a[i] 
        i += 1
        k += 1
    while (j < m): 
        res[k] = b[j] 
        j += 1
        k += 1
 
    res.sort() 

a = str(input('Enter list a:')) 
b = str(input('Enter list b:')) 
n = len(a) 
m = len(b) 

res = [0 for i in range(n + m)] 
sortedMerge(a, b, res, n, m) 
print ("Sorted merged list :")
for i in range(n + m): 
    print (res[i]) 