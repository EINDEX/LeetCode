import re

class Solution:
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        if not queries:
            return []
        trans_re = re.compile('[AaEeIiOoUu]')
        res = []
        dic = set(wordlist)
        
        change_dict = {}
        for word in wordlist:
            t = word.lower()
            if t not in change_dict:
                change_dict[t] = word
        
        word_dict = {}
        for word in wordlist:
            t = trans_re.sub('_',word).lower()
            if t not in word_dict:
                word_dict[t] = word
                
        for query in queries:
            if query in dic:
                res.append(query)
            else:
                l = query.lower()
                if l in change_dict:
                    res.append(change_dict[l])
                    continue
                t = trans_re.sub('_',query).lower()
                if t in word_dict:
                    res.append(word_dict[t])
                else:
                    res.append('')
        return res
            
        
