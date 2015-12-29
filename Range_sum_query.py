# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.


class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
        self.updatedlist = []
        self.updateList()

    def updateList(self):
        if len(self.nums) >0:
            self.updatedlist.append(self.nums[0])
        for i in range(1,len(self.nums)):
            self.updatedlist.append(self.updatedlist[i-1] + self.nums[i])


    def sumRange(self, i, j):
        sum = self.updatedlist[j]
        if i >=1:
            sum -= self.updatedlist[i-1]
        return sum



# Your NumArray object will be instantiated and called as such:

# numArray = NumArray(nums)

# numArray.sumRange(0, 1)

# numArray.sumRange(1, 2)
