class Solution(object):
	def wordPattern(self, pattern, str):
		str_list = str.split(' ')
		if not len(str_list) == len(pattern):
			return False
		pattern_dict = {}
		for i in xrange(len(str_list)):
			if str_list[i] not in pattern_dict.values() and pattern[i] not in pattern_dict.keys():
				pattern_dict[pattern[i]] = str_list[i]
				continue
			if not pattern_dict.get(pattern[i]) == str_list[i]:
				return False
		return True
