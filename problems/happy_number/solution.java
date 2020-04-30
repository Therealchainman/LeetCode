class Solution {
    private HashSet<Integer> setty = new HashSet<>();
    public boolean isHappy(int n) {
                int sum = 0;
        if (n == 1) {
            return true;
        }
        if (setty.contains(n)) {
            return false;
        }
        setty.add(n);
        while (n > 0) {
            sum += Math.pow(n%10, 2);
            n = n/10;
        }
        return isHappy(sum);
    }
}