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

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        buckets = [ [] for i in range(len(nums) + 1) ]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for n, c in count.items():
            buckets[c].append(n)
        
        res = []

        for bucket in range(len(buckets) - 1, 0, -1):
            for n in (buckets[bucket]):
                print(n)
                res.append(n)
                if len(res) == k:
                    return res
        
        # print(buckets)
test = Solution().topKFrequent(nums = [1,1,1,2,2,3,7], k = 2)