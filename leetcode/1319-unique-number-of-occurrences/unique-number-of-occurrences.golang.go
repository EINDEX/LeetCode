func uniqueOccurrences(arr []int) bool {
    c := make(map[int]int, len(arr))
    for _, x := range arr {
        if _, ok := c[x]; !ok {
            c[x] = 1
        } else {
            c[x]++
        }
    }

    r := make(map[int]int, len(c))
    for _, v := range c {
        if _, ok := r[v]; !ok {
            r[v] = 1
        } else {
            return false
        }
    }
    return true
}