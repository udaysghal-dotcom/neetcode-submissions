class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for i in range(len(strs)):
            sorted_str = tuple(sorted(strs[i]))
            
            if sorted_str not in anagram_map:
                anagram_map[sorted_str] = []
            
            anagram_map[sorted_str].append(strs[i])

        result = []
        for key in anagram_map:
            result.append(anagram_map[key])
        
        return result
