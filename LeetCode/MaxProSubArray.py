# Maximum Product of Sub 
class Solution:
    def maxProSubArray(self , nums: list[int]) -> int:
        res = max(nums)
        currMin , currMax = 1,1

        for n in nums:
            if n==0:
                currMin , currMax= 1 ,1
                continue
            tmp = currMax*n
            currMax = max(currMax*n , currMax , currMin*n)
            currMin = max(tmp , currMin*n , n)
            res = max(res , currMax)
        return res 