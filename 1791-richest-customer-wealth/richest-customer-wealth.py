class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for person in accounts:
            current_wealth = 0
            
            for money in person:
                current_wealth = current_wealth + money
                
                if current_wealth > max_wealth:
                    max_wealth = current_wealth

        return max_wealth        