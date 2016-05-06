'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

'''
* if O(1) space asked, use another O(n) loop to check whether repeated or not
M1:
Brute Force: O(n**3) time O(n) space
for each pair of position , check whether it is repeated or not
M2: O(n**3) time O(n) space
for each char, check longest unrepeated substring start from the char
M3: O(n) time O(n) space
1) set head pointer to indicate longest unrepeated substring ending at current char
2) use hash table map with (char, postion) pair
3) if current char exists in current substring, reset head pointer to next repeated char in substring
'''

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() < 2) { // boundary cases
            return s.length();
        }
        int res = 0;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int head = 0;
        map.put(s.charAt(0), 0);
        for (int i = 1; i < s.length(); i++) {
            if (map.containsKey(s.charAt(i)) && map.get(s.charAt(i)) >= head) { // current char exists in current longest substring
                head = map.get(s.charAt(i)) + 1;
            }
            map.put(s.charAt(i), i); // need to update s.charAt(i) whether map contains or not
            if (res < (i - head + 1)) { // update res if current substring is longer
                res = i - head + 1;
            }
        }
        return res;
    }
}
