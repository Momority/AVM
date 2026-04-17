from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
            
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, frequency in count.items():
            buckets[frequency].append(num)
      
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result

if __name__ == "__main__":
    sol = Solution()
    
    # Тест 1
    print("(nums=[1,1,1,2,2,3], k=2):", sol.topKFrequent([1,1,1,2,2,3], 2))
    
    # Тест 2
    print("(nums=[1], k=1):", sol.topKFrequent([1], 1))
    
    # Тест 3
    test3_nums = [1,2,1,2,1,2,3,1,3,2]
    print(f"(k=2):", sol.topKFrequent(test3_nums, 2))