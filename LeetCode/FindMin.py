# Find Minimum in rotated Sub Array
# [3,4,5,1,2]
class Solution:
    def findmin(self, nums:list[int]) -> int:
        res = nums[0]
        l,r = 0, len(nums)-1

        while l<=r:
            if nums[l] < nums[r]:
                res = min(res , nums[l])
                break
            m = (l+r) //2
            res = min(res , m)
            if nums[m] >= nums[l]:
                l = m +1
            else:
                r = m-1
        return res
    
print(Solution().findmin([3,4,5,1,2]))