class Solution(object):
    def addOperators(self, nums, target):
        self.r_l = []
        self.target = target
        self.op_list = ['*', '-', '+'] 
        for i in xrange(1, len(nums)+1):
            new_op_num = nums[:i]
            if new_op_num.startswith('00'):
                continue
            self.dp_search(nums[i:], nums[:i])
        return self.r_l
    
    def dp_search(self, nums_remain, operator_str):
        if not nums_remain:
            result = eval(operator_str)
            if result == self.target:
                self.r_l.append(operator_str)
        else:
            for op in self.op_list: 
                for i in xrange(1, len(nums_remain)+1):
                    new_op_num = nums_remain[:i]
                    new_nums_remain = nums_remain[i:]
                    if new_op_num.startswith('00'):
                        continue
                    operator_str_new = ''.join([operator_str, op, new_op_num])
                    self.dp_search(new_nums_remain, operator_str_new)

if __name__ == '__main__':
    s = Solution()
    import sys
    nums = sys.argv[1]
    target = sys.argv[2]
    print s.addOperators(nums, int(target))
