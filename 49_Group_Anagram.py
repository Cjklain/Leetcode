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


# asd = Solution2().groupAnagrams(["act", "pots", "tops", "cat", "stop", "haat"])
# print(asd)
# print(("asd", "asd") == ("asd", "asd"))

# there is a place for impovments


class Solution3:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        closet = {}
        result = []
        for str in strs:
            temp = "".join(sorted(str))
            if temp in closet:
                closet[temp].append(str)
            else:
                closet[temp] = [str]

        for item in closet.values():
            result.append(item)

        return result


qwe = Solution3().groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"])
# print(qwe)


class Solution4:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}

        for s in strs:
            print(sorted(s))

        for s in strs:
            sor = "".join(sorted(s))
            if sor in d:
                d[sor].append(s)
            else:
                d[sor] = [s]

        result = []

        for i in d:
            result.append(d[i])

        return result

        print(result)


# qwe = Solution4().groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"])
# print(qwe)

from collections import defaultdict


class Solution5:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        storage = defaultdict(list)

        for str in strs:
            sorted_str = "".join(sorted(str))
            storage[sorted_str].append(str)

        return list(storage.values())


qwedqw = Solution5().groupAnagrams([""])
print(qwedqw)


class Solution5:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        storage = defaultdict(list)

        for str in strs:
            letter_key = [0] * 26
            for letter in str:
                letter_key[ord(letter) - ord("a")] += 1
            storage[tuple(letter_key)].append(str)

        print(storage)
        return list(storage.values())


qwedqw = Solution5().groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"])
print(qwedqw)
