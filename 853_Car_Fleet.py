class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        data = []
        stack = []
        for i, pos in enumerate(position):
            cycles = (target - pos) / speed[i]
            data.append((pos, cycles))

        print(data)
        data = sorted(data)
        print(data)

        for el in data[::-1]:
            if not stack or el[1] > stack[-1][1]:
                stack.append(el)

        print(stack)
        return len(stack)


test = Solution()
test.carFleet(target=10, position=[1, 4], speed=[3, 2])
