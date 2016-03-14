import math
class Solution(object):
	table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	def titleToNumber(self, s):
		total = 0
		for i in xrange(len(s)):
			index = self.table.index(s[i])+1
			print index*math.pow(26, len(s)-i-1)
			total += index*math.pow(26, len(s)-i-1)
		return int(total)

if __name__ == '__main__':
	sl = Solution()
	print sl.titleToNumber('CCC')
			
