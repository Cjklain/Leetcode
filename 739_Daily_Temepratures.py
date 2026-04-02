class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        results = [0 for el in temperatures]
        for i, el in enumerate(temperatures):
            while stack and stack[-1][0] < el:
                stack_el, stack_i = stack.pop()
                results[stack_i] = i - stack_i
            stack.append((el, i))
        print(results)


asd = Solution()
asd.dailyTemperatures([30, 38, 30, 36, 35, 40, 28])
