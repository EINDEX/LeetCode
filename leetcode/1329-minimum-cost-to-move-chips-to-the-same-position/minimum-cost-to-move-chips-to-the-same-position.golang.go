func minCostToMoveChips(chips []int) int {
    even, odd := 0, 0
    for _, chip := range chips {
        if chip % 2 == 0 {
            even ++
        } else {
            odd ++
        }
    }
    if odd < even {
        return odd
    } else {
        return even
    }
}