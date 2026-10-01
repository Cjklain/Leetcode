# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         dictForNums = {}
#         arrToReturn = []
#         for num in nums:
#             if num in dictForNums:
#                 dictForNums[num] += 1
#             else:
#                  dictForNums[num] = 1
#         for _ in range(k):
#             # print(max(dictForNums, key=dictForNums.get))
#             temp = max(dictForNums, key=dictForNums.get)
#             arrToReturn.append(temp)
#             del dictForNums[temp]
#         return arrToReturn

# test_old = Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2)

# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         count = {}
#         buckets = [ [] for i in range(len(nums) + 1) ]

#         for num in nums:
#             count[num] = 1 + count.get(num, 0)

#         for n, c in count.items():
#             buckets[c].append(n)

#         res = []

#         for bucket in range(len(buckets) - 1, 0, -1):
#             for n in (buckets[bucket]):
#                 print(n)
#                 res.append(n)
#                 if len(res) == k:
#                     return res

#         print(buckets)
# test = Solution().topKFrequent(nums = [1,1,1,2,2,3,7], k = 2)


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        counted = {}
        heap = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            if num in counted:
                counted[num] += 1
            else:
                counted[num] = 1

        for key, value in counted.items():
            heap[value].append(key)

        res = []
        for i in range(len(heap) - 1, 0, -1):
            for n in heap[i]:
                res.append(n)
                if len(res) == k:
                    return res


# group list in hashmap
# find k times max
# resturn


class Solution2:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        data = {}
        freq = [[] for i in range(len(nums) + 1)]
        for item in nums:
            if item in data:
                data[item] += 1
            else:
                data[item] = 1

        for num in data:
            freq[data[num]].append(num)

        result = []

        for element in range(len(freq) - 1, 0, -1):
            temp = freq[element]
            for el in temp:
                result.append(el)
                if len(result) == k:
                    return result
        # print(freq)

        print(result)
        # for el in reversed(freq):
        #     temp = len(el)
        #     i = 0
        #     while k > 0 and temp > i:
        #         result.append(el[i])
        #         i = i + 1
        #         k = k - 1

        return result
        # print(result)
        # print(freq)
        # print(data)


asd = Solution2().topKFrequent([1, 2, 2, 3, 3, 3], 2)
print(asd)


class Solution3:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        print("asd")
        counter = {}

        helper_arr = [[] for _ in range(len(nums)) + 1]

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        print(counter)

        for val in counter:
            helper_arr[counter[val]].append(val)

        print(helper_arr)

        res = []

        print(len(helper_arr))
        print(range(len(helper_arr)))

        for x in range(len(helper_arr)):
            print(x)

        for i in range(len(helper_arr) - 1, 0, -1):
            for n in helper_arr[i]:
                res.append(n)
                if k == len(res):
                    return res


# zxc = Solution3().topKFrequent([1, 2, 2, 3, 3, 3, 3], 2)


class Solution4:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        result = []
        data = [None] * (len(nums) + 1)
        helper = {}

        for num in nums:
            if helper.get(num):
                helper[num] += 1
            else:
                helper[num] = 1

        print(result, data, helper)

        for asd in helper:
            if data[helper[asd]]:
                print(data[helper[asd]])
                data[helper[asd]].append(asd)
            else:
                data[helper[asd]] = [asd]

        for el in data[::-1]:
            if el:
                for e in el[::-1]:
                    result.append(e)
                    k = k - 1

                    if k <= 0:
                        return result


zxc2 = Solution4().topKFrequent([7, 7], 1)
print(zxc2)
