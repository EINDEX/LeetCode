# Guess Numbers

## Difficulty
Easy

## Question
<p>English description is not available for the problem. Please switch to Chinese.<br />
&nbsp;</p>


## Solution
### python3
```python3
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return sum([guess[i]==answer[i] for i in range(3)])
```

## Author
EINDEX