from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
        
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid  
            
            if nums[mid] < target:
              
                left = mid + 1
            else:
                
                right = mid - 1
       
        return -1

if __name__ == "__main__":
    sol = Solution()
    
    # Тест 1
    nums1, target1 = [-1, 0, 3, 5, 9, 12], 9
    print(f"{sol.search(nums1, target1)}")  # 4
    
    # Тест 2
    nums2, target2 = [-1, 0, 3, 5, 9, 12], 2
    print(f"{sol.search(nums2, target2)}")  # -1