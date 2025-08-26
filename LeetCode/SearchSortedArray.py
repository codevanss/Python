# Search in rotated subarray
# [4,5,6,7,0,1,2]
class Solution:
    def search(self, nums:list[int] , target)->int :
        l,r = 0 , len(nums)-1
        target = target
        while l <=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            #Left sorted array
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target <nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1