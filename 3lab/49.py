from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)
            
        return list(ans.values())
if __name__ == "__main__":
    solution = Solution()
    
    test_data = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = solution.groupAnagrams(test_data)
    
    print("Входные данные:", test_data)
    print("Результат группировки:", result)

    print("Пример с пустой строкой:", solution.groupAnagrams([""]))