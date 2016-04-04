class Solution(object):
	def isInterleave(self, s1, s2, s3):
		if len(s1) + len(s2) != len(s3):
			return False
		if (not s2 and s1 == s3) or (not s1 and s2 == s3):
			return True
		if s1 and s2 and s1[0] == s2[0] and s2[0] == s3[0]:
			return self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:])
		elif s1 and s1[0] == s3[0]:
			return self.isInterleave(s1[1:], s2, s3[1:])
		elif s2 and s2[0] == s3[0]:
			return self.isInterleave(s1, s2[1:], s3[1:])
		else:
			return False

if __name__ == '__main__':
	s = Solution()
	#import sys
	#s1 = sys.argv[1]
	#s2 = sys.argv[2]
	#s3 = sys.argv[3]

	s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
	s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
	s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
	print s.isInterleave(s1,s2,s3)
