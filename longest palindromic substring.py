'''
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one 
unique longest palindromic substring.
'''
'''
Brute Force: O(n**2) time O(1) space
1) for each position, check the longest palindromic substring use it as center
'''
public class Solution {
    private int longest= 1;
    private int start = -1;
    private int end = -1;
    public String longestPalindrome(String s) {
        if (s.length() < 2) {
            return s;
        }
        for (int i = 0; i < (s.length() - longest/2); i++) {
            explore(s, i, i);
            explore(s, i, i + 1);
        }
        return s.substring(start + 1, end);
    }
    public void explore(String s, int left, int right) {
        while (left > -1 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        if (longest < (right - left - 1)) {
            longest = right - left - 1;
            start = left;
            end = right;
        }
    }
}
