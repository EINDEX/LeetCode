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

