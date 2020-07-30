"""
    Program to take input from user and create array of a particular length.
    Also ignore the second index element from the array.
"""

from array import *
import time

print("Please give the input properly ----> It is case sensitive.")
time.sleep(2)
l = int(input("\nsigned int=1\nunsigned int=2\nEnter the type of  array from listed above : "))

"""Checks for the input and if incorrect input is given then error message is displayed"""

if l == 1:
    arr=array('i',[])
elif l==2:
    arr = array('I', [])
else:
    print("Give valid input!!!!")

# Program to enter the size of the array
n = int(input("Enter the length of the array : "))

# Then we run a for loop to take the input of elements of the array
# And for the element at index 2 we skip the value else we append the values to array
for i in range(n):
    val = int(input("Enter the value of element : "))
    if i==2:
        continue
    else:
        arr.append(val)

# We further convert array to list to display the elements in the proper sequence as entered by the user
list = arr.tolist()
print("The elements of the array are : ",list)