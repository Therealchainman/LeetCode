func maxProfit(prices []int) int {
    if len(prices)==0 {
        return 0
    }
	max_profit:=0
	min_up_to_index:=prices[0]
    cur_max_profit:=0
	for i:=1;i<len(prices);i++ {
		cur_max_profit=prices[i]-min_up_to_index
		if cur_max_profit>0 {
			max_profit=Max(cur_max_profit,max_profit)
		}
		min_up_to_index=Min(min_up_to_index,prices[i])
	}
	return max_profit
}

func Max(x,y int) int {
	if x > y {
		return x
	}
	return y
}

func Min(x,y int) int {
	if x < y {
		return x
	}
	return y 
}