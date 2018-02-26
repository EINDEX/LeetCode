func singleNumber(nums []int) int {
	res := 0
	for i, x := range nums {
		print(i)
		res ^= x
	}
	return res
}
