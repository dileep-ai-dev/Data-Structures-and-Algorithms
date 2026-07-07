def recursive_search(arr,low,high,target):

    if low>high:
        return -1

    mid=low+(high-low)//2

    if arr[mid]==target:
        return mid

    elif arr[mid]>target:
        return recursive_search(arr,low,mid-1,target)

    else:
        return recursive_search(arr,mid+1,high,target)

arr=[1,2,3,4,4,5]
print(recursive_search(arr,0,len(arr)-1,5))