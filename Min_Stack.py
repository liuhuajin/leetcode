class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if len(self._stack) == 0:
            self._stack.append((x,x))
        else:
            t = self._stack[-1]
            x_pair = (x, x if x < t[1] else t[1])
            self._stack.append(x_pair)

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self._stack):
            x = self._stack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        if len(self._stack):
            return self._stack[-1][0]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if len(self._stack):
            return self._stack[-1][1]
        return None
