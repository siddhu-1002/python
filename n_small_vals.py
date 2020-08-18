# Program to print n small values of the list

m = int(input("How many elements do you want to add to your list : "))        # Taking input from user about how many values to be added into list
numbers = []                                                                  # Created an empty list to add the input input values from the user

for term in range(1,m+1):
    element = int(input("Enter the element of the list : "))
    numbers.append(element)

dup_num = numbers.copy()
n = int(input("How many small values do you want to print : "))               # Taking input from user about how many minimum values to be printed

for i in range(1, n+1):
    low1 = min(dup_num)
    ind1 = numbers.index(low1)
    dup_num.remove(low1)
    print(f"Index of {i}th minimum value is : ", numbers[ind1])
