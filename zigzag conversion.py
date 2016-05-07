'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility) 
P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows: 
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". 
'''
'''
M1: math O(n) time O(1) space
'''
public class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1) {
            return s;
        }
        StringBuffer res = new StringBuffer();
        for (int i = 0; i < numRows; i++) {
            int start = i;
            if (i == 0 || i == (numRows - 1)) {
                while (start < s.length()) { // careful about condition while loop, in case of dead loop
                    res.append(s.charAt(start));
                    start += (numRows - 1) * 2;
                }
            }
            else {
                while (start < s.length()) {
                    res.append(s.charAt(start));
                    start += (numRows - i - 1) * 2;
                    if (start >= s.length()) {
                        break;
                    }
                    res.append(s.charAt(start));
                    start += i * 2;
                }
            }
        }
        return res.toString();
    }
}
'''
M2: BF O(n) time O(n) space
'''
public String convert(String s, int nRows) {
    char[] c = s.toCharArray();
    int len = c.length;
    StringBuffer[] sb = new StringBuffer[nRows];
    for (int i = 0; i < sb.length; i++) sb[i] = new StringBuffer();

    int i = 0;
    while (i < len) {
        for (int idx = 0; idx < nRows && i < len; idx++) // vertically down
            sb[idx].append(c[i++]);
        for (int idx = nRows-2; idx >= 1 && i < len; idx--) // obliquely up
            sb[idx].append(c[i++]);
    }
    for (int idx = 1; idx < sb.length; idx++)
        sb[0].append(sb[idx]);
    return sb[0].toString();
}
