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