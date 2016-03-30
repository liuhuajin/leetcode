class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
		
class Solution(object):
	def getIntersectionNode(self, headA, headB):
		lenA = lenB = 0 
		head = headA
		while head:
			head = head.next
			len += 1
		head = headB
		while head:
			head = head.next
			len += 1
		head1, head2 = (headA, headB) if lenA > lenB else (headB, headA)
		delta = lenA - lenB if lenA > lenB else lenB - lenA
		while delta:
			head1 = head1.next
		while not head1.val == head2.val:
			head1 = head1.next
			head2 = head2.next
		return head1
