func pathInZigZagTree(label int) []int {

    var res []int
	for ; label > 0; {
		res = append(res, label)
		label = label >> 1
	}
	sort.Sort(sort.IntSlice(res))
	for i := len(res) - 2; i > 0; i -= 2 {
		res[i]=3*int(math.Pow(float64(2), float64(i))) - res[i] - 1
	}
    return res
}