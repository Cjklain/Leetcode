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
