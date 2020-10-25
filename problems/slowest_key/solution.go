func slowestKey(releaseTimes []int, keysPressed string) byte {
    var kx = keysPressed[0]
    var mx = releaseTimes[0]
    var n=len(releaseTimes)
    for i:=1;i<n;i++ {
        var cand = releaseTimes[i]-releaseTimes[i-1]
        var ch = keysPressed[i]
        if cand>mx || (cand==mx && kx<ch) {
            kx=ch
            mx=cand
        } 
    }
    return kx
}