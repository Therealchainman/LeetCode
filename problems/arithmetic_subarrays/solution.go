

func checkArith(nums []int) bool {
    var n=len(nums)
    sort.Ints(nums)
    if n<=2 {
        return true
    }
    var diff = nums[1]-nums[0]
    for i:=2;i<n;i++ {
        var new_diff = nums[i]-nums[i-1]
        if new_diff!=diff {
            return false
        }
    }
    return true
    
}
func checkArithmeticSubarrays(nums []int, l []int, r []int) []bool {
    // var n = len(nums)
    var m = len(l)
    var ans = []bool{}
    for i:=0;i<m;i++ {
        var left = l[i]
        var right = r[i]
        nnums:=append([]int(nil), nums...)
        pnums := nums[left:right+1]
        nums=nnums
        if checkArith(pnums) {
            ans=append(ans,true)
        } else {
            ans=append(ans,false)
        }
    }
    
    return ans
}