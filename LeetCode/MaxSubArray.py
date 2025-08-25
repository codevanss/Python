class Solution:
    def maxSubArray(self , nums: list[int]) -> int:
        maxSub = nums[0]
        currSum = 0 

        for i in nums:
            if currSum < 0:
                currSum = 0
            currSum += i
            maxSub = max(currSum , currSum)
        return maxSub