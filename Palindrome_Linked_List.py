class Solution(object):
    def isPalindrome(self, head):
    	link_len = 0
    	real_head = head
    	if not head:
    		return True
    	while head:
    		head = head.next
    		link_len += 1
    	half = link_len/2 if link_len %2 == 0 else (link_len+1)/2
    	i = 0
    	new_head = real_head
    	for i in xrange(half):
    		new_head = new_head.next
    	r_head = None
    	while new_head:
    		temp = new_head
    		new_head = new_head.next
    		temp.next = r_head
    		r_head = temp
    	head = real_head
    	while r_head:
    		if not r_head.val == head.val:
    			return False
    		r_head = r_head.next
    		head = head.next
    	return True
