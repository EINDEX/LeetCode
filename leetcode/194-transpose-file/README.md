# Transpose File

## Difficulty
Medium

## Question
<p>Given a text file <code>file.txt</code>, transpose its content.</p>

<p>You may assume that each row has the same number of columns, and each field is separated by the <code>&#39; &#39;</code> character.</p>

<p><strong>Example:</strong></p>

<p>If <code>file.txt</code> has the following content:</p>

<pre>
name age
alice 21
ryan 30
</pre>

<p>Output the following:</p>

<pre>
name alice ryan
age 21 30
</pre>



## Solution
### bash
```bash
# Read from the file file.txt and print its transposed content to stdout.
python3 -c 'print("\n".join(map(" ".join,zip(*map(str.split,open("file.txt").readlines())))))'
```