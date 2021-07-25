class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        nums = list(num)
        flag = False
        for n in range(len(nums)):
            k = int(nums[n])
            if change[k] > k:
                nums[n]= str(change[k])
                flag = True
            elif flag and change[k] == k:
                continue
            elif flag:
                break
           
        return ''.join(nums)