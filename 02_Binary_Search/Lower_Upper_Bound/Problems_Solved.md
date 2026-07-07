
Find First and Last Position of Element in Sorted Array
----------------------------------------------------------

PROBLEM STATEMENT:
------------------

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
    
If target is not found in the array, return [-1, -1].

-------------------------------------------------------------------


CODE:
-----

def lower_bound(nums,target):
        low,high=0,len(nums)-1

        while low<=high:
            mid=low+(high-low)//2

            if nums[mid]<target:
                low=mid+1
            else:
                high=mid-1

        return low

def upper_bound(nums,target):
        low,high=0,len(nums)-1

        while low<=high:
            mid=low+(high-low)//2

            if nums[mid]<=target:
                low=mid+1
            else:
                high=mid-1
            
       
        return low-1

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        lb=lower_bound(nums,target)
        ub=upper_bound(nums,target)
        
        if lb>ub:
            return [-1,-1]
        return [lb,ub]




        