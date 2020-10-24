class Solution {
    public int bagOfTokensScore(int[] tokens, int P) {
        Arrays.sort(tokens);
        int maxScore = 0, score = 0;
        int l = 0, r = tokens.length - 1;
        while(l <= r && P >= tokens[l]) {
            while(l < tokens.length && P >= tokens[l]) {
                P -= tokens[l++];
                score++;
            }
            maxScore = Math.max(maxScore, score);
            if(score > 0 && l <= r) {
                P += tokens[r--];
                score--;
            }
        }
        return maxScore;
    }
}