func countSegments(s string) int {
    counter := 0
    flag := true
    for _, x := range s {
        if x != ' ' && flag{
            flag = false
            counter += 1
        } else if x == ' ' {
            flag = true
        }
    }
    return counter
}