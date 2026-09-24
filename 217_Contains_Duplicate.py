class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) > pow(10, 5):
            return
        for i in range(len(nums)):
            print(nums[i], "a")
            # print(i, 'a')
            for j in range(1, len(nums) - i):
                if nums[i] == nums[-j]:
                    return True
                print(j, nums[-j], "b")
        return False
        # for k


class Solution1:
    def containsDuplicate(self, nums: list[int]) -> bool:
        record_list = {}
        if len(nums) > pow(10, 5):
            return
        for num in nums:
            if num in record_list:
                # print(num)
                return True
            record_list[num] = 1
        return False


from collections import defaultdict


class Solution2:
    def containsDuplicate(self, nums: list[int]) -> bool:
        collection = defaultdict()
        for num in nums:
            if num in collection:
                return True
            collection[num] = 1

        return False


class Solution3:
    def containsDuplicate(self, nums: list[int]) -> bool:
        collection = {}
        for num in nums:
            if num in collection:
                return True
            collection[num] = None

        print(collection)
        return False


class Solution4:
    def containsDuplicate(self, nums: list[int]) -> bool:
        collection = set()
        for num in nums:
            if num in collection:
                return True
            collection.add(num)

        return False


test = Solution4()

# print(test.containsDuplicate(nums = [2,14,18,22,22]))
# print(test.containsDuplicate(nums = [1,2,3,4]))


# print(test.containsDuplicate(nums=[2, 14, 18, 22, 22]))


class Solution5:
    def containsDuplicate(self, nums: list[int]) -> bool:

        collection = set()

        for num in nums:
            collection.add(num)

        if len(collection) != len(nums):
            return True
        else:
            return False


# asd = Solution5().containsDuplicate([1,1,3])


class Solution6:
    def containsDuplicate(self, nums: list[int]) -> bool:

        collection = defaultdict()

        for num in nums:
            if num in collection:
                return True
            collection[num] = 1

        return False


# asd = Solution6().containsDuplicate([1,1,3])


class Solution7:
    def containsDuplicate(self, nums: list[int]) -> bool:
        test = set()
        for num in nums:
            if num in test:
                return True
            test.add(num)
        return False


asd = Solution7().containsDuplicate([1, 2, 3, 1])
# print(asd)


# 12min
class Solution8:
    def containsDuplicate(self, nums: list[int]) -> bool:
        data = {}

        for num in nums:
            if num in data:
                return True
            else:
                data[num] = 1

        return False


# asd2 = Solution8()
# print(asd2.containsDuplicate([1, 2, 3, 5]))


class Solution9:
    def hasDuplicate(self, nums: list[int]) -> bool:
        helper = {}

        for num in nums:
            if num in helper:
                return True
            else:
                helper[num] = 1

        return False


asd4 = Solution9().hasDuplicate([1, 2, 3, 3])
print(asd4, "asd")
