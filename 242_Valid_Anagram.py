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
# print(test1)
# print(test2)


class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        asd = "zxc"
        # asd2 = slice(len(asd), 0, -1)
        # print(asd[::-1])
        if s[::-1] == t:
            return True
        else:
            return False


# test3 = Solution3()
# test5 = test3.isAnagram(s="anagram", t="nagaram")
# print(test5)


class Solution4:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or len(s) >= 5 * 100000:
            return False
        tempS = {}
        tempT = {}

        for letter in s:
            tempS[letter] = tempS.get(letter, 0) + 1

        for letter in t:
            tempT[letter] = tempT.get(letter, 0) + 1

        print(tempS, tempT)

        if tempS == tempT:
            return True

        return False


asd = Solution4().isAnagram("racecar", "carrace")
print(asd)
