def isBadVersion(n):
	return n == 2

class Solution(object):
	def firstBadVersion(self, n):
		low = 1
		high = n
		while low <= high:
			mid = int((low+high)/2)
			print '-----'
			print low, high, mid
			if isBadVersion(mid):
				if mid == 1 or not isBadVersion(mid-1):
					return mid
				else:
					high = mid - 1
			else:
				low = mid + 1
		return n

if __name__ == '__main__':
	s = Solution()
	import sys
	n = int(sys.argv[1])
	print s.firstBadVersion(n)
