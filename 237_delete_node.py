class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def deleteNode(self, Node):
		Node.val = Node.next.val
		Node.next = Node.next.next
