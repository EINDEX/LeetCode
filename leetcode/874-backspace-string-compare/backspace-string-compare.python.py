class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def get_res(string):
            num = 0
            res = ''
            for x in string[::-1]:
                if x == '#':
                    num += 1
                else:
                    if num:
                        num -= 1
                    else:
                        res += x
            return res
        return get_res(T) == get_res(S)

