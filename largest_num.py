class Solution(object):
	def largestNumber(self, nums):
		nums.sort(cmp= lambda x, y: int(str(y)+str(x)) - int(str(x)+str(y)))
		result = ''.join([str(x) for x in nums])
		for i in xrange(len(result)):
			if not result[i] == '0' or i == len(result):
				break
		return result[i:]

if __name__ == '__main__':
	s = Solution()
	nums = [0,0,0]
	print s.largestNumber(nums)
