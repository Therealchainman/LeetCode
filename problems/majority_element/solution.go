func majorityElement(nums []int) int {
	n := len(nums) / 2
	count := make(map[int]int)
	for _, elem := range nums {
		count[elem]++
		if count[elem] > n {
			return elem
		}
	}
	return -1
}