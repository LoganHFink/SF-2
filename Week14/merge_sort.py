def merge(left,right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j< len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])    
    return result

def mergeSort(lst):
    if len(lst) == 1:
        return lst
    
    mid = len(lst) // 2
    left_half = lst[:mid] 
    right_half = lst[mid:]

    sorted_left = mergeSort(left_half)
    sorted_right = mergeSort(right_half)

    return merge(sorted_left,sorted_right)

print(mergeSort([1,4,7,9,24,8,1,5]))