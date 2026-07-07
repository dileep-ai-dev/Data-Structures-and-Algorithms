# UPPER_BOUND

def upper_bound(arr,target):
    low,high=0,len(arr)-1

    while low<=high:
        mid=low+(high-low)//2

        if arr[mid]<=target:
            low=mid+1
        else:
            high=mid-1

    return low



# Time Complexity: O(log n)

# Space Complexity: O(1)