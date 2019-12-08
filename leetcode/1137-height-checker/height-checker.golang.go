func heightChecker(heights []int) int {
    cpyHeights := make([]int, len(heights))
    copy(cpyHeights, heights)
    sort.Ints(cpyHeights)
    res := 0
    for i := 0; i < len(heights); i++ {
        if heights[i] != cpyHeights[i] {
            res ++
        }
    }
    return res 
}