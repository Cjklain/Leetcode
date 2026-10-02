class Solution:

    def encode(self, strs: list[str]) -> str:
        crypted = []
        for word in strs:
            crypted.append(f"{len(word)}#{word}")
        return "".join(crypted)

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0
        j = ""
        while i < len(s):
            if s[i] == "#":

                result.append(s[i + 1 : i + 1 + int(j)])
                i = i + int(j)
                j = ""
            else:
                j = j + s[i]
            i = i + 1

        return result


asd = Solution().encode(["Hello", "world"])
asd2 = Solution().decode(asd)


# test = [1, 23, 4, 56]
# result = []
# result.append(test[1:3])
# print(result)
class Solution2:
    def encode(self, strs: list[str]) -> str:
        result = ""
        for str in strs:
            result = f"{result}{len(str)}#{str}"
        return result

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0
        while len(s) > i:
            j = i
            while s[j] != "#":
                j += 1
            letter_number = int(s[i:j])
            result.append(s[j + 1 : j + 1 + letter_number])
            i = j + 1 + letter_number
        return result


qwe = Solution2().encode(["neet", "code", "love", "you"])


# print(qwe)
# qwe2 = Solution2().decode(qwe)
# print(qwe2)
class Solution3:
    def encode(self, strs: list[str]) -> str:
        result = ""

        for s in strs:
            # print(s)
            result = result + str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> list[str]:
        result = []

        j = 0
        i = 0
        while i < len(s):
            if s[i] == "#":
                s_length = int(s[j:i])
                i = i + 1
                result.append(s[i : i + s_length])
                i = i + s_length
                j = i
            i = i + 1

        return result


sqwe = Solution3().encode(["Hello", "World"])
print(sqwe)
qwe2 = Solution3().decode(sqwe)
print(qwe2)
