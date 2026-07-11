def is_possible(mid,piles,h):
    total=0
    for i in range(len(piles)):
        total+=ceil(piles[i]/mid)
    return total<=h


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low=1
        high=max(piles)
        ans=0
        while low<=high:

            mid=low+(high-low)//2
            if is_possible(mid,piles,h):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
