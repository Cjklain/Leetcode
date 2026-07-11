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
