def last_occurrence(arr, target):

    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == target:
            ans = mid
            low = mid + 1

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return ans