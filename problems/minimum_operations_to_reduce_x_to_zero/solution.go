func min(a int, b int) int {
    if a>b {
        return b
    }
    return a
}

func minOperations(nums []int, x int) int {
    n := len(nums)
    prefixSize:=0
    suffixSize:=0
    MAX := 100000
    ret:=MAX
    xf := 0
    for i:=n-1;i>=0;i-- {
        if xf+nums[i]<=x {
            suffixSize++
            xf+=nums[i]
        } else {
            break
        }
    }
    if xf==x {
        ret = suffixSize
    }
    for i:=0;i<n;i++ {
        xf+=nums[i]
        for suffixSize>0 && xf>x {
            xf-=nums[n-suffixSize]
            suffixSize--
        }
        if suffixSize<0 {
            break
        }
        prefixSize=i+1
        if xf==x {
            ret=min(ret,prefixSize+suffixSize)
        }
    }
    if ret<=n {
        return ret
    }
    return -1
}