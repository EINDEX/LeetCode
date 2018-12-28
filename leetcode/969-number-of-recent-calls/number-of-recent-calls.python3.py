class RecentCounter:

    def __init__(self):
        self.pings = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.pings.append(t)
        for i in range(len(self.pings)):
            if self.pings[i] >= t-3000:
                break
        
        for x in range(i-1, -1, -1):
            self.pings.pop(x)
            
        return len(self.pings)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)