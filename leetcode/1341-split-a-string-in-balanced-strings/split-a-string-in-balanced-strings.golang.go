func balancedStringSplit(s string) int {
    num := 0
    res := 0
    for _, x := range s {
        if x == 'R' {
            num ++
        } else {
            num --
        }
        if num == 0 {
            res ++
        }
    }
    return res
}