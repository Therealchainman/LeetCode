func possible(target int, value int) bool {
    return value <= target
}

func binarySearch(target int, nums []int, start int, end int) int {
    lo := start
    hi := end
    var mid int
    for lo < hi {
        mid = (lo + hi + 1)>> 1
        if possible(target, nums[mid]) {
            lo = mid
        } else {
            hi = mid - 1
        }
    }
    return lo
}

func possibleNotEqual(target int, value int) bool {
    return value < target
}

func binarySearchNotEqual(target int, nums []int, start int, end int) int {
    lo := start
    hi := end
    var mid int
    for lo < hi {
        mid = (lo + hi + 1)>> 1
        if possibleNotEqual(target, nums[mid]) {
            lo = mid
        } else {
            hi = mid - 1
        }
    }
    return lo
}

func binarySearchLowerBound(target int, nums []int, start int, end int) int {
    lo := start
    hi := end
    var mid int
    for lo < hi {
        mid = (lo + hi)>> 1
        if possibleNotEqual(target, nums[mid]) {
            lo = mid + 1
        } else {
            hi = mid
        }
    }
    return lo
}

func setSliceValue(val int, slice []int) {
    for i:=0;i<len(slice);i++ {
        slice[i]=val
    }
}


func maximizeXor(nums []int, queries [][]int) []int {
    sort.Ints(nums)
    n := len(queries)
    ans := make([]int, n)
    setSliceValue(-1,ans)
    for j:=0;j<n;j++ {
        x := queries[j][0]
        m := queries[j][1]
        if m < nums[0] {
            continue
        }
        best := 0
        start := 0
        cur := 0
        end := binarySearch(m, nums,start,len(nums)-1)
        // for i, y := range nums {
        //     fmt.Println(i,y^x)
        // }
        // fmt.Println(nums)
        for i:=31;i>=0;i-- {
            bit := 1 << i
            // fmt.Println(start, end)
            if (x & bit) > 0 {
                // fmt.Println(bit)
                if (nums[start]&bit)==0 {
                    // fmt.Println(bit)
                    best |= bit
                    // fmt.Println(best)
                    end = binarySearchNotEqual(cur | bit, nums, start, end)
                    // fmt.Println(end)
                } else {
                    cur |= bit
                }
            } else {
                if (nums[end] & bit) > 0 && end>=start {
                    // fmt.Println("zero hero")
                    // fmt.Println(bit)
                    best |= bit
                    cur |= bit
                    // fmt.Println(best)
                    start = binarySearchLowerBound(cur,nums,start,end)
                    // fmt.Println(start)
                }
            }
        }
        ans[j]=best
    }
    return ans
}