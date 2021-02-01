func reverse(i int, j int, nums []int) {
    for i < j {
        nums[i], nums[j] = nums[j], nums[i]
        i++
        j--
    }
}

func nextPermutation(nums []int)  {
    n := len(nums)
    var i int
    for i=n-2;i>=0;i-- {
        if nums[i]<nums[i+1] {
            break
        }
    }
    if i>=0 {
        var j int
        for j=n-1;j>i;j-- {
            if nums[j]>nums[i] {
                nums[i],nums[j]=nums[j],nums[i]
                break
            }
        }
        reverse(i+1,n-1,nums)
    } else {
        reverse(0,n-1,nums)
    }
}