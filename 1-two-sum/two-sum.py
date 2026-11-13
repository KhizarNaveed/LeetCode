class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        # enumerate function bascially loops over a list and gives you both the index and the value at the exact same time
        
        for i, num in enumerate(nums):
            needed = target - num

        # Is the complement already in the dictionary?

            if needed in seen:
                return [seen[needed], i]
         
        # If not, save the current number and its index into 'seen' 
            seen[num] = i    