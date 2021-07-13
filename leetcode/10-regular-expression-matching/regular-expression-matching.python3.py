import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return bool(re.compile(p).fullmatch(s))