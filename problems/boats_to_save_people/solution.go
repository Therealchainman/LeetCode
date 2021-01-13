func numRescueBoats(people []int, limit int) int {
    sort.SliceStable(people, func(i, j int) bool {
        return people[i]>people[j];
    })
    i:=0
    n:=len(people)
    j:=n-1
    for i=0;i<n && i<=j; i++ {
        if people[i]+people[j]<=limit {
            j--
        }
    }
    return i
}