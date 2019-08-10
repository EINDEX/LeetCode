func convert(s string, numRows int) string {
    rows := make([]string, numRows)
    index, godown := 0, true
    if numRows == 1{
        return s
    }
    for _, x := range s {
        rows[index] += string(x)
        if godown {
            index += 1
        } else {
            index -= 1   
        }
        if index >= numRows {
            godown = false
            index = numRows - 2
        } else if index < 0 {
            godown = true
            index = 1
        }
    }
    res := ""
    for _, x := range rows{
        res+=x
    }
    return res
}