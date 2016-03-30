class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def removeElements(self, head, val):
		new_head = ListNode('new')
		new_head.next = head
		thead = new_head
		while thead.next:
			if thead.next.val == val:
				thead.next = thead.next.next
			else:
				thead = thead.next
			if not thead:break
		return new_head.next

if __name__ == '__main__':
	s = Solution()
	head = ListNode(1)
	head.next = a = ListNode(2)
	# a.next = b = ListNode(2)
	# b.next = c = ListNode(2)
	# c.next = d = ListNode(2)
	# d.next = e = ListNode(2)
	val = 1
	head = s.removeElements(head, val)
	print '>>>>>>>>>>>>>>>>>>>>>>'
	while head:
		print head.val
		head = head.next
