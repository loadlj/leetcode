class Solution(object):
    def twoSum(self, nums, target):
        waiting_dict = {}
        result = list()
        for i, j in enumerate(nums, 1):
            if j in waiting_dict:
                result.append((waiting_dict[j], i))
            else:
                waiting_dict[target-nums[i-1]] = i
        return result

if __name__ == '__main__':
    s = Solution()
    l = [1, 2, 3, 4, 5]
    print s.twoSum(l, :)
