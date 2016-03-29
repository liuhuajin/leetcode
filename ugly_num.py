class Solution(object):
	def isUgly(self, num):
		if num == 0:
			return False
		while num % 2 == 0:
			num = num / 2
		while num % 3 == 0:
			num = num / 3
		while num % 5 == 0:
			num = num / 5
		return  num == 1

if __name__ == '__main__':
	import sys
	num = int(sys.argv[1])
	s = Solution()
	print s.isUgly(num)
