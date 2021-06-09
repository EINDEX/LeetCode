class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        @lru_cache(None)
        def dfs(idx, p, pro):
            if idx == len(group):
                return int(pro == minProfit)
            # 剩余人数不足以参加第idx个任务
            if 0 <= p < group[idx]:
                return dfs(idx+1,p,pro)
            # 使用min(minprofit, pro + profit[idx])主要是为了减少记录的状态数，不再记录大于minfit的状态           
            return dfs(idx+1,p-group[idx],min(minProfit, pro+profit[idx]))+dfs(idx+1,p,pro)

        return dfs(0,n,0) % (10**9+7)
