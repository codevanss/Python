class Solution: 
    def twoSum(self,nums:list[int], target:int) -> list[int]:
        prevMap = {}

        for i , n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff] , i ]
            prevMap[n] = i

nums = [2, 7, 11, 15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target))



# Two Difference

class Solution:
    def twoDiff(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}  # store number : index

        for i, n in enumerate(nums):
            # Check if n - target exists
            if (n - target) in prevMap:
                return [i, prevMap[n - target]]
            # Store current number with index
            prevMap[n] = i
sol = Solution()
nums = [5, 20, 3, 2, 50, 80]
target = 78
print(sol.twoDiff(nums, target))
