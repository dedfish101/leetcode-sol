class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramdict = {}
        for s in strs:
            key = tuple(sorted(s))

            if key not in anagramdict:
                anagramdict[key] = []

            anagramdict[key].append(s)
        return list(anagramdict.values())
