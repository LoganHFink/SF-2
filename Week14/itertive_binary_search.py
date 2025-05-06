def binarySearch(lst,target):

    low = 0
    mid = len(lst)
    high = 0

    while low <= high:
        mid = (low + high)//2
        high = len(lst) -1

        if lst[mid] < target:
            low = mid+1
        elif lst[mid] > target:
            high = mid-1
        else:
            return mid

lst = [1,2,1,4,5,3,7,8]
print(binarySearch(lst,3))