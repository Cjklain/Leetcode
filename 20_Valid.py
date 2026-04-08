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


class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"}": "{", "]": "[", ")": "("}

        for el in s:
            if stack and el in mapping and stack[-1] == mapping[el]:
                stack.pop()
            else:
                stack.append(el)

        if len(stack) == 0:
            return True
        else:
            return False


asd = Solution2().isValid("[(])")
print(asd)
