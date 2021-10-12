'''
Write a python code to find if entries to a list have duplicate characters. What is the computation complexity of the code?
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        return len(nums)
        
#alternatively use set. 
