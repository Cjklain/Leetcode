class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        s2 = "".join(sorted(s))
        t2 = "".join(sorted(t))
        if s2 == t2:
            return True
        return False


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        for letter in s:
            if letter in sdict:
                sdict[letter] += 1
            else:
                sdict[letter] = 1

        for tLetter in t:
            if tLetter in sdict:
                if sdict[tLetter] > 1:
                    sdict[tLetter] -= 1
                    continue
                if sdict[tLetter] == 1:
                    del sdict[tLetter]
            else:
                return False

        if not sdict:
            return True
        else:
            return False


test = Solution()
test1 = test.isAnagram(s="anagram", t="nagaram")
test2 = test.isAnagram(s="rat", t="car")
print(test1)
print(test2)
