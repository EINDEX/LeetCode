class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = [0 for _ in range(10)]
        b = [0 for _ in range(10)]
        bulls = 0
        for x in range(len(secret)):
            if secret[x] != guess[x]:
                a[int(secret[x])] += 1
                b[int(guess[x])] += 1
            else:
                bulls += 1
        cows = sum([min(a[x], b[x]) for x in range(10) if a[x] > 0 and b[x] > 0])
           
        return f'{bulls}A{cows}B'