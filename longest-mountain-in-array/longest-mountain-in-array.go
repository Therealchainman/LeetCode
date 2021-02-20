func longestMountain(nums []int) int {
    n, cnt,ans := len(nums),0,0
    seenPeak := false
    for i:=1;i<n;i++{
        if i==1 && (nums[i]>nums[i-1] || nums[i-1]>nums[i]) { // just starting with either increasing or decreasing segment at start of length 2
            cnt = 2
        } else {
            if nums[i]>nums[i-1] && nums[i-1]<=nums[i-2] {  // dreasing or flat segment of length 2  followed by increasing segment of length 2 
                cnt=2
                seenPeak=false
            } else if nums[i]==nums[i-1] { // flat surface
                cnt=0
            } else if (nums[i]>nums[i-1] && nums[i-1]>nums[i-2]) || (nums[i]<nums[i-1] && nums[i-1]<nums[i-2]) { // increasing or decreasing segment of length 3
                cnt++
            } else if nums[i]<nums[i-1] && nums[i-1]>nums[i-2] { // increasing segment of length 2 followed by decreasing segment of length 2
                cnt++
                seenPeak = true
            }
        }
        if seenPeak {
            ans=max(cnt,ans)
        }
    }
    return ans
}

func max(x, y int) int {
    if x > y {return x}
    return y
}