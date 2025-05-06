def binarySearch(lst,low,high,target):
    if low <= high:
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] <= target:
            return binarySearch(lst, mid+1, high, target)
        else:
            return binarySearch(lst, low, mid-1, target)

lst = [2,3,5,7,11,33]
print(binarySearch(lst,0,len(lst)-1,5))        
