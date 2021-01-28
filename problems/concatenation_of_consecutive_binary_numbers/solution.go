func concatenatedBinary(n int) int {
	mod := int64(1e9 + 7)
	var ans int64

	for i := 1; i <= n; i++ {
		size := digits(i)
		ans = ((ans << size) | int64(i)) % mod
	}

	return int(ans)
}

func digits(i int) int {
	var shift int
	for shift = 31; (1<<shift)&i == 0; shift-- {
        
	}
	return shift + 1
}