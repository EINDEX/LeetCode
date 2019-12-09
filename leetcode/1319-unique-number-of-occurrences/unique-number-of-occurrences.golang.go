func uniqueOccurrences(arr []int) bool {
    c := map[int]int{}
    for _, x := range arr {
        c[x]++
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