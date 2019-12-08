func subtractProductAndSum(n int) int {
    m := 1
    s := 0
    for ;n > 0; {
        a := n % 10
        s += a
        m *= a
        n /= 10
    }
    return m - s
}