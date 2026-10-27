class Solution:
    def twoSum(self,nums,target):
        seen={}
        for i in range(len(nums)):
            needed=target-nums[i]

            if needed in seen:
                return [seen[needed],i]
                break
            seen[nums[i]]=i    
