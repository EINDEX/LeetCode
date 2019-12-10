func Dfs(res *[]int, i, max int) {
	if i > max {
		return
	}
	*res = append(*res, i)
	for j := 0; j < 10; j++ {
		Dfs(res, i*10+j, max)
	}
}

func lexicalOrder(n int) []int {
    res := make([]int, 0)
	for i := 1; i <= n && i < 10; i++ {
		Dfs(&res, i, n)
	}
    return res
}