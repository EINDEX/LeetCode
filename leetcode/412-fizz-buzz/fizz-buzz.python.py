class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for x in range(1, n+1):
            if x % 15 == 0:
                res.append("FizzBuzz")
            elif x % 5 == 0:
                res.append("Buzz")
            elif x % 3 == 0:
                res.append("Fizz")
            else:
                res.append(str(x))
            
            
        return res

