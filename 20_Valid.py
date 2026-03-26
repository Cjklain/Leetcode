class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        mapping = {")": "(", "]": "[", "}": "{"}
        stack = []

        for el in s:
            if len(stack) >= 1 and el in mapping and stack[-1] == mapping[el]:
                del stack[-1]
            else:
                stack.append(el)

        if len(stack) > 0:
            return False

        return True


asd = Solution().isValid("([)]")
print(asd)
