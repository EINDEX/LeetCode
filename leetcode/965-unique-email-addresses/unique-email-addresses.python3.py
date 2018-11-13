class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = set()
        for email in emails:
            local, host = email.split('@')
            res.add(local.split('+')[0].replace('.','')+'@'+host)
        return len(res)
            