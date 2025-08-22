class Solution:

    def containDuplicate(self, nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    

# Second approach

list1 = [1,2,32]
freq = {}
for i in list1:
    freq[i] = freq.get(i , 0)+1
for key in freq:
    if freq[key] >1:
        print("True")
        break
    else:
        print("false")
        break
    
