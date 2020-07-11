class Solution:
    def reformatDate(self, date: str) -> str:
        m = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
        d = date.split()
        if len(d[0]) == 3:
            d[0] = d[0][:1]
        else:
            d[0] = d[0][:2]
        da = f"{d[2]}-{int(m[d[1]]):02}-{int(d[0]):02}"
        return da