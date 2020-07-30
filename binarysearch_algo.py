def binary_search(list,v):
    l = 0
    u = len(list) - 1
    while l != u:           #If value of lower and upper limit differ then enter the loop
        m = (l+u)//2
        if list[m] < v:     #If the mid-value is smaller than value to be found
            l = m+1         #then change the lower limit
        else:               #If the mid-value is larger than value to be found
            u = m-1         #then change the upper limit

    if 0 <= l <len(list) and list[l] == v:
        print("Value found at : ", l)
    else:
        print("Value not found")

binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 54)