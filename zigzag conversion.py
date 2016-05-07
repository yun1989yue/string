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
