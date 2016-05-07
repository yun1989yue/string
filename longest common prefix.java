/*
Write a function to find the longest common prefix string amongst an array of strings. 
*/

// M1: O(mn) time O(1) space
// use a parameter to record position of longest common prefix
public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        int common = strs[0].length(); // common prefix has at most length as shortest str
        for (int i = 1;i < strs.length;i++) {
            for (int j = 0;j < common;j++) {
                if (j >= strs[i].length()) { // two cases to update common, 1st: different char in same position, 2nd: smaller str
                    common = j;
                    break;
                }
                if (strs[i].charAt(j) != strs[0].charAt(j)) {
                    common = j;
                }
            }
        }
        return strs[0].substring(0, common);
    }
}
// M2: O(mn) time O(1) space
// use indexOf and descending length to find common prefix
public String longestCommonPrefix(String[] strs) {
    if(strs == null || strs.length == 0)    return "";
    String pre = strs[0];
    int i = 1;
    while(i < strs.length){
        while(strs[i].indexOf(pre) != 0)
            pre = pre.substring(0,pre.length()-1);
        i++;
    }
    return pre;
}
