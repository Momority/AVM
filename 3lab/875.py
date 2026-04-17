import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        left = 1
        right = max(piles)
        
        result = right
        
        while left <= right:
            k = (left + right) // 2
            
            total_time = 0
            for p in piles:
            
                total_time += math.ceil(p / k)
            
            if total_time <= h:
                result = k      
                right = k - 1    
            else:
                left = k + 1    
                
        return result

if __name__ == "__main__":
    sol = Solution()
    
    # Тест 1
    print(f"(piles=[3,6,7,11], h=8): {sol.minEatingSpeed([3,6,7,11], 8)}") # 4
    
    # Тест 2
    print(f"(piles=[30,11,23,4,20], h=5): {sol.minEatingSpeed([30,11,23,4,20], 5)}") #  30
    
    # Тест 3
    print(f"(piles=[30,11,23,4,20], h=6): {sol.minEatingSpeed([30,11,23,4,20], 6)}") # 23