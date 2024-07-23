class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        dict_for_anagrams = {}
        for i, str in enumerate(strs):
            temp = ''.join(sorted(str))
            if temp in dict_for_anagrams:
                dict_for_anagrams[temp].append(i)
            else:
                dict_for_anagrams[temp] = [i]
        
        sorted_anagrams = []
        for dic in dict_for_anagrams:
            temp2 = []
            for dic2 in dict_for_anagrams[dic]:
                # print(strs[dic2])
                temp2.append(strs[dic2])
            sorted_anagrams.append(temp2)
            # print(dict_for_anagrams[dic])
        print(sorted_anagrams)

test = Solution().groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]) 