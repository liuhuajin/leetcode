class NumArray(object):
    def __init__(self, nums):
    	self.nums_sum = [nums[0]] if len(nums) else []
        self.nums = nums
        for i in xrange(1, len(nums)):
        	n_sum = self.nums_sum[i-1] + nums[i]
        	self.nums_sum.append(n_sum)

    def sumRange(self, i, j):
    	return self.nums_sum[j] - self.nums_sum[i] + self.nums[i]
