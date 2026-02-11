class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        dict_for_anagrams = {}
        for i, str in enumerate(strs):
            temp = "".join(sorted(str))
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


# test = Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])


class Solution2:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        test = {}
        result = []
        for input_str in strs:
            str_sorted = "".join(sorted(input_str))
            if str_sorted in test:
                test[str_sorted].append(input_str)
            else:
                test[str_sorted] = [input_str]

            # print(str_sorted)

        for k, item in test.items():
            result.append(item)

        return result


asd = Solution2().groupAnagrams(["act", "pots", "tops", "cat", "stop", "haat"])
print(asd)
# print(("asd", "asd") == ("asd", "asd"))
