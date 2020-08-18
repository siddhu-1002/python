# Program to reverse array
from array import array
import time

n=int(input("Enter the length of the array : "))   # Take the length of array the user wants to enter
arr=array('i',[])

for i in range (n):          # Running a for loop to take input of values from user
    val = int(input("Enter the value : "))
    arr.append(val)

arr2=array('i',[])
for j in range(n-1,-1,-1):
    arr2.append(arr[j])

print("\nThe array after reverse is : ",arr2)