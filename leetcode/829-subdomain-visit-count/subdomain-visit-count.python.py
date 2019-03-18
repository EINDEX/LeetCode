class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        res = {}
        for x in cpdomains:
            times, domain = x.split(' ')
            subdomain = domain.split('.')
            for x in range(len(subdomain)):
                d = '.'.join(subdomain[x:])
                res.setdefault(d,0)
                res[d] += int(times)
        return ["%d %s" % (times,domain) for domain,times in res.items()]
            
        
