func diStringMatch(S string) []int {
    m, M := 0, len(S)
    res := make([]int, M+1)
    for i, v := range S {
        if v == 'D' {
            res[i] = M
            M--
        } else {
            res[i] = m
            m++
        }
    }
    res[len(S)] = M
    return res
}