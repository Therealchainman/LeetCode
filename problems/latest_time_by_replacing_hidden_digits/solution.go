func maximumTime(time string) string {
    x := time[0]
    y := time[1]
    z := time[3]
    w := time[4]
    if w=='?' {
        w = '9'
    }
    if z =='?' {
        z = '5'
    }
    if y=='?' {
        if x=='0' || x=='1' {
            y = '9'
        } else {
            y = '3'
        }
    }
    if x == '?' {
        if y=='0' || y=='1' || y=='2' || y=='3' {
            x = '2'
        } else {
            x = '1'
        }
    }
    return fmt.Sprintf("%v%v:%v%v", x-'0', y-'0', z-'0', w-'0')
}