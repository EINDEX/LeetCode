class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        length = len(strs)
        
        flag = True
        res = ""
        index = 0
        while flag:
            temp = ""
            for x in range(length):
                if len(strs[x]) > index:
                    if not temp:
                        temp = strs[x][index]
                    else:
                        if temp != strs[x][index]:
                            return res
                else:
                    return res
            else:
                res += temp
            index += 1
                    
                
        

