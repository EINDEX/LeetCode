# Max Consecutive Ones

## Difficulty
Easy

## Question
<p>Given a binary array <code>nums</code>, return <em>the maximum number of consecutive </em><code>1</code><em>&#39;s in the array</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,0,1,1,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,0,1,1,0,1]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>



## Solution
### golang
```golang
func findMaxConsecutiveOnes(nums []int) int {
	max := 0
	count := 0
	flag := false

	for _, v := range nums {
		if v == 0 {
			flag = false
		} else {
			if !flag {
				flag = true
				count = 0
			}
			count += 1
			if count > max {
				max = count
			}
		}
	}

	return max
}


```
### python3
```python3
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = 0
        count = 0
        flag = True
        for x in nums:
            if x == 0:
                flag = False
            else:
                if not flag:
                    count = 0
                count += 1
                flag = True
                if count > max_value:
                    max_value = count
        return max_value

```