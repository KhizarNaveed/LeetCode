class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        arr = []
        sum = 0

        for i in nums:
            sum = sum + i
            arr.append(sum)
        return arr    