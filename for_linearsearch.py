from typing import Any
"""
    Imported any for accepting any kind of values, In this case Integer.
    Created a function linear_search with two parameters : 'lst'-->Iterable
    and 'value' to be searched.
"""

def linear_search(lst, value):

    """
        We run a for loop in range of length of list which is 10 in this case.
        If-statement is used to check if the  i_th element is equal to the value to be searched.
        If the condition is true then the function returns 'i'.
        Else the value of i gets incremented until it is greater than len(list).
    """

    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


lst = [1,21,5,3,1,2,4,5,6,4]

"""
    The return value of the function gets stored in variable 'j'.
    Finally we get the output as the index value of 1.
"""

j = linear_search(lst, 1)
print(j)