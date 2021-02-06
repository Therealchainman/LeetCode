func simplifyPath(path string) string {
    var stk []string
    var str []byte
    dots := 0
    for i:=0;i<len(path);i++ {
        if path[i] == '/' && dots > 0 && len(str) == dots {
            if dots == 2 && len(stk) > 0 {
                stk = stk[:len(stk)-1]
            } else if dots > 2 {
                stk = append(stk, string(str))
            } 
            dots = 0
            str = nil
        }
        if path[i] != '.' {
            dots = 0
        }
        if path[i] == '/' && len(str) > 0 {
            stk = append(stk, string(str))
            str = nil
        } else if path[i] == '/' {
            continue
        } else if path[i] == '.' {
            dots++
            str = append(str, path[i])
        } else {
            str = append(str, path[i])
        }
    }
    if dots > 0 && len(str) == dots {
        if dots == 2 && len(stk) > 0 {
            stk = stk[:len(stk)-1]
        } else if dots > 2 {
            stk = append(stk, string(str))
        } 
        dots = 0
        str = nil
    }
    if len(str) > 0 {
        stk = append(stk, string(str))
    }
    var canon string
    for _, s := range stk {
        canon += "/" + s
    }
    if len(canon) == 0 {
        return "/"
    }
    return canon
}