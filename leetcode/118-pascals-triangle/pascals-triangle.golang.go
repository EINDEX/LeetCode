func generate(numRows int) [][]int {
	res := make([][]int, numRows)
	for r := 0; r < numRows; r++ {
		res[r] = make([]int, r+1)
		if r == 0 {
			res[0][0] = 1
		} else {
			for i := 0; i < r+1; i++ {
				if (i == 0) || (i == r) {
					res[r][i] = 1
				} else {
					res[r][i] = res[r-1][i] + res[r-1][i-1]
				}
			}
		}
	}
	return res
}


