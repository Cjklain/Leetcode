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
            print(el)
            if stack and el in mapping and stack[-1] == mapping[el]:
                stack.pop()
            else:
                stack.append(el)

        if len(stack) == 0:
            return True
        else:
            return False


# asd = Solution2().isValid("[(])")
# print(asd)


class Solution3:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"}": "{", "]": "[", ")": "("}

        if len(s) % 2 != 0:
            return False

        for el in s:
            if stack and el in mapping and stack[-1] == mapping[el]:
                stack.pop()
            else:
                stack.append(el)

        if len(stack) == 0:
            return True
        else:
            return False


# asx = Solution3().isValid("(])(])")
# print(asx)


class Solution4:
    def isValid(self, s: str) -> bool:
        helper_stack = []
        helper_dict = {"(": ")", "{": "}", "[": "]"}

        for el in s:
            if el in helper_dict:
                helper_stack.append(el)
            else:
                if helper_stack and el == helper_dict[helper_stack[-1]]:
                    helper_stack.pop()
                else:
                    return False

        if helper_stack:
            return False
        else:
            return True


asxaa = Solution4().isValid("))))))")
print(asxaa)
