import numpy as np

print('масс')

arr=[]

r,l=i
if arr[l]<arr[r]: r+=1
else: 
    l+=1
    l=r
curr = sum(arr[r:l])
best = max(best, curr) 