
#14.03.2026 question -1

class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i,n in enumerate(nums):
            if target-n in d:
                return [d[target-n],i]
            d[n]=i

nums=list(map(int,input().split()))
target=int(input())

s=Solution()
print(s.twoSum(nums,target))
