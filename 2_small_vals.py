#Program to find index of two smallest values using [Find index Remove element Find index Algorithm]

"""
    Created original list named 'count'
    Created a copy of original list as 'counts'
"""
count = [809, 834, 67, 478, 307, 100, 122, 123, 324, 476]
counts = count.copy()

"""
    We first print the index of minimum value in the list 'counts'
    We then remove it from the list.
"""

low1 = min(counts)
ind1 = counts.index(low1)
counts.remove(counts[ind1])

"""
    We then print the index of another minimum value in the list 'counts'
"""

min(counts)
low2 = min(counts)
ind2 = counts.index(low2)

"""
    If index is greater than or equal to the index of first value than we
    increment it by 1 because we have removed the 1st lowest value from the list.
"""
if ind2 >=ind1:
    ind2 += 1
else:
    pass
"""Now we print the index and value of 1st and 2nd minimum value"""

print("Index of first minimum value is : ", ind1, "and the value is : ", count[ind1])
print("Index of second minimum value is : ", ind2, "and the value is : ", count[ind2])
