class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # using built-in function but interview rejects that
        # s.reverse()
        
        s[:] = s[::-1]
