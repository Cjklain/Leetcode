class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s2 = "".join(sorted(s))
        t2 = "".join(sorted(t))
        if s2 == t2:
            return True
        return False


test = Solution()
test1 = test.isAnagram(s="anagram", t="nagaram")
test2 = test.isAnagram(s="rat", t="car")
print(test1)
print(test2)
