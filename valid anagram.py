'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets
'''
'''
hashtable O(n) time O(n) space
1) for each character in s, push it into hash and assign 1 if not exist, else add 1
2) for each character in t, push it into hash and assign -1 if not exist, else minus 1\
3) if a character in hash has value rather than 0, return False, else True
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        used = {}
        for i in xrange(len(s)):
            if s[i] not in used:
                used[s[i]] = 1
            else:
                used[s[i]] += 1
            if t[i] not in used:
                used[t[i]] = -1
            else:
                used[t[i]] -= 1
        for item in used:
            if used[item] != 0:
                return False
        return True
        
'''
Array
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        chars = [0]*26
        for i in xrange(len(s)):
            chars[ord(s[i]) - ord('a')] += 1 # ord can transform characters to int accordign to ascii
            chars[ord(t[i]) - ord('a')] -= 1
        for item in chars:
            if item != 0:
                return False
        return True
