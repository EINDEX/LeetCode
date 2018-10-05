class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stash = []
        self.min_helper = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stash.append(x)
        if not self.min_helper:
            self.min_helper.append(len(self.stash) - 1)
        elif x < self.getMin():
            self.min_helper.append(len(self.stash) - 1)
        

    def pop(self):
        """
        :rtype: void
        """
        self.stash.pop()
        if self.min_helper[-1] == len(self.stash):
            self.min_helper.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stash[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stash[self.min_helper[-1]]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()