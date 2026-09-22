class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            char_count = [0] * 26

            for c in word:
                char_count[ord(c) - ord("a")] += 1
            
            anagram_map[tuple(char_count)].append(word)
        
        return list(anagram_map.values())