class Solution(object):
	def findPeakElement(self, nums):
		low = 0
		high = len(nums)-1
		while low <= high:
			mid = int((low + high)/2)
			larger_than_left = (mid == 0) or (mid > 0 and nums[mid-1] < nums[mid])
			larger_than_right = (mid == len(nums)-1) or (mid < len(nums)-1 and nums[mid] > nums[mid+1])
			if larger_than_left and larger_than_right:
				return mid
			elif larger_than_left:
				low = mid + 1
			else:
				high = mid - 1
		return -1

if __name__ == '__main__':
	s = Solution()
	nums = [3,2,1]
	print s.findPeakElement(nums)
