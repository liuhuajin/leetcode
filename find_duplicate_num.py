class Solution(object):
	def findDuplicate(sef, nums):
		low, high = 1, len(nums)-1
		while low <= high:
			mid = (low + high) / 2
			mid_smaller_num = sum ( x <= mid for x in nums)
			if mid_smaller_num > mid:
				high = mid - 1
			else:
				low = mid + 1
		return low
