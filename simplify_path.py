class Solution(object):
	def simplifyPath(self, path):
		path_list =  path.split('/')
		real_path = []
		print path_list
		for x in path_list:
			if x == '.' or x == '':
				continue
			elif x == '..':
				if real_path:
					real_path.pop(-1)
			else:
				real_path.append(x)
			print '------'
			print real_path
		return '/' + '/'.join(real_path)

if __name__ == '__main__':
	import sys
	s = Solution()
	path = sys.argv[1]
	print 'test %s'%path
	result = s.simplifyPath(path)
	print 'result'
	print result
