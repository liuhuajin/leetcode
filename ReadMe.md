##NOTE:
纪录一些题解

###Find Duplicate Numbr
解法：时间复杂度O(n * log n)

[来源](https://leetcode.com/problems/find-the-duplicate-number/)


二分查找（Binary Search）+ 鸽笼原理（Pigeonhole Principle）

“不允许修改数组” 与 “常数空间复杂度”这两个限制条件意味着：禁止排序，并且不能使用Map等数据结构

小于O(n2)的运行时间复杂度可以联想到使用二分将其中的一个n化简为log n

参考LeetCode Discuss：https://leetcode.com/discuss/60830/python-solution-explanation-without-changing-input-array

二分枚举答案范围，使用鸽笼原理进行检验

根据鸽笼原理，给定n + 1个范围[1, n]的整数，其中一定存在数字出现至少两次。

假设枚举的数字为 n / 2：

遍历数组，若数组中不大于n / 2的数字个数超过n / 2，则可以确定[1, n /2]范围内一定有解，

否则可以确定解落在(n / 2, n]范围内。

###maxinum product of word lengths
[来源](https://leetcode.com/problems/maximum-product-of-word-lengths/)

一开始想到了排序，然后从大到小进行遍历，但是仍然超时，后来在每次判断是否有相同字符之前，先判断是否乘积大于目前的最大值，可以AC,目前看来，排序并没有什么用处。

网上的题解：

位运算来判断是否含有相同的字符

### Minimum Size Subarray Sum
思路不难，把计算当前段加和的函数替换下就可以了，o(n)复杂度可解

### Find Peak Element

[来源](https://leetcode.com/problems/find-peak-element/)

[参考](https://siddontang.gitbooks.io/leetcode-solution/content/array/find_peak_element.html)

提到对数复杂度的时候就应该直接想到二分，关于为什么用二分一定能找到值的原因，参见下面：

首先我们找到中间节点mid，如果大于两边返回当前index就可以了，如果左边的节点比mid大，那么我们可以继续在左半区间查找，这里面一定存在一个peak，为什么这么说呢？假设此时的区间范围为[0, mid - 1]， 因为num[mid - 1]一定大于num[mid]了，如果num[mid - 2] <= num[mid - 1]，那么num[mid - 1]就是一个peak。如果num[mid - 2] > num[mid - 1]，那么我们就继续在[0, mid - 2]区间查找，因为num[-1]为负无穷，所以最终我们绝对能在左半区间找到一个peak。同理右半区间一样。
