class Solution(object):
	def lowestCommonAncestor(self, root, p, q):
		if root == None or root == p or root == q:
			return root
		left = self.lowestCommonAncestor(root.left, p, q)
		right = self.lowestCommonAncestor(root.right, p, q)
		if left and right:
			return root
		if left:
			return left
		return right
