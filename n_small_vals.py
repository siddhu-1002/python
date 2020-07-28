#Program to find index of n smallest values using [Find index Remove element Find index Algorithm]
# Taking input from user about how many minimum values to be printed
n = int(input("How many small values do you want to print : "))
"""
    Created original list named 'count'
    Created a copy of original list as 'counts'
"""
numbers = [809, 834, 67, 478, 307, 100, 122, 123, 324, 476]
dup_num = numbers.copy()


for i in range(1, n+1):
    low1 = min(dup_num)
    ind1 = numbers.index(low1)
    dup_num.remove(low1)
    print(f"Index of {i}th minimum value is : ", numbers[ind1])