class Solution(object):
	def reverse(self, x):
		flag = 1 if x >= 0 else -1
		_x = abs(x)
		_x_list = str(_x)
		_x_list = _x_list[::-1]
		t = 0
		for i in xrange(len(_x_list)):
			if _x_list[i] != 0 or i == len(_x_list) - 1:
				t = i
				break
		_list = _x_list[t:]
		str_x = ''.join(_list)
		n = int(str_x)*flag
		print n
		print 0x7fffffff
		print 0x80000000
		if n > 0x7fffffff or n < -0x80000000:
			n = 0
		return n

if __name__ == '__main__':
	s = Solution()
	import sys
	num = sys.argv[1]
	print s.reverse(int(num))
		
