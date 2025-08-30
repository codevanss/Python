class Solution:
    def hammingweight(self , n:int)->int:
        res = 0
        while n >0:
            res += n%2
            n = n >>1
        return res


class Solution:
    def hammingweight(self , n:int)->int:
        res = 0
        while n >0:
            n= n&(n-1)
            res+=1
        return res