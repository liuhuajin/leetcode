class Solution(object):
	def isPowerOfTwo(self, num):
		if num == 0:
			return False
		while num % 2 == 0:
			num = num / 2
		return num == 1
