# Program to implement bubble sort algorithm
'''
    In this algorithm, we compare successive values of the sequence
    taken two at a time.
    We compare the values and if 1st value is greater than 2nd value we
    swap them else we increment the index by one and this continues till
    we reach the end of the sequence.
    This process continues till the whole list is sorted.
'''

ls = [10,50,40,90,70,102,65,302,11,57,654,103,325,3]

for i in range(len(ls)-1):
    for j in range(len(ls)-1):
        if ls[j] < ls[j+1]:
            continue
        else:
            ls[j+1],ls[j] = ls[j] , ls[j+1]

print("\nThe sorted list is :|\n "
      "                   V\n", ls)