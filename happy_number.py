#-*- encoding:utf-8 -*-

class Solution(object):
    def isHappy(self, n):
        used_nums = []
        while True:
            used_nums.append(n)
            n_str_list = str(n)
            n_sum = 0
            for c in n_str_list:
                n_sum += int(c)*int(c)
            if n_sum == 1:
                return True
            if n_sum in used_nums:
                break
            n = n_sum
        return False

if __name__ == '__main__':
    s = Solution()
    import sys
    n = int(sys.argv[1])
    print s.isHappy(n)
