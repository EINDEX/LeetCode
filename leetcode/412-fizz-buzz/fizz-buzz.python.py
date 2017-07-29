class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in xrange(1, n+1)]
        ans = []
        for x in xrange(1,n+1):
            a = ''
            if not x % 3:
                a += 'Fizz'
            if not x % 5:
                a += 'Buzz'
            if not a:
                a = str(x)
            ans.append(a)
        return ans
        