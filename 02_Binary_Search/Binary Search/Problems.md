# Binary Search Problems

## Easy

- [
- 




    class Solution:
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
- [




    class Solution:
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

###  Search a 2D Matrix
- [  


    class Solution:
        def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            m=len(matrix)
            n=len(matrix[0])
            low=0
            high=(n*m-1)
            while low<=high:
                mid=low+(high-low)//2
                row=mid//n
                column=mid%n
    
                if matrix[row][column]==target:
                    return True
                elif matrix[row][column]<target:
                    low=mid+1
                else:
                    high=mid-1
            return False

        ] 