func convert(s string, numRows int) string {
    if numRows == 1 || len(s) < numRows {
        return s
    }
    rows := make([]string, numRows)
    index, godown := 0, true

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