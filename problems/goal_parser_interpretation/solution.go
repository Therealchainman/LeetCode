func interpret(command string) string {
    ans := ""
    i := 0
    for i<len(command) {
        if command[i]=='G' {
            ans+="G"
            i++
        } else if command[i]=='(' && command[i+1]==')' {
            ans+="o"
            i+=2
        } else {
            ans+="al"
            i+=4
        }
    }
    return ans
}