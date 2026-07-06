# Binary Search Problems

## Easy

- [class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low,high=0,len(nums)-1

        while low<=high:
            mid=low+(high-low)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1

        return -1 ] LeetCode 704 - Binary Search
- [class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low,high=0,len(nums)-1

        while low<=high:
            mid=low+(high-low)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1

        return low ] LeetCode 35 - Search Insert Position

## Medium

- [ ] (Will be added in future lessons)