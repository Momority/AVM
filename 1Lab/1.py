def unique(array):
    return len(set(array)) == len(array)

array1 = [1, 2 ,3 ,4]
array2 = [1, 2, 2, 3]
array3 = []

print(unique(array1))
print(unique(array2))
print(unique(array3))