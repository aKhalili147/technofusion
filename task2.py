"""
    DESCRIPTION:

        Given array {2,3,6,6,8,9,10,10,10,12,12}  is already sorted, and it has duplicate elements.
        Write a program to remove duplicate elements and return new array without any duplicate elements. 
        The array should contain only unique elements.

"""

# test arr
arr_srted = [2,3,6,6,8,9,10,10,10,12,12] # array with duplicated values
arr = []                                 # array not duplicated values

for el in arr_srted:
    if el not in arr:
        arr.append(el)

print(arr)
