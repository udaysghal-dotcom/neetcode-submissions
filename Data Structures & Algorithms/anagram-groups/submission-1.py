class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            sorted_str = sorted(s)
            anagram_map[tuple(sorted_str)].append(s)
        
        return list(anagram_map.values())