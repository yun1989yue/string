'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''
'''
M1: stack O(n) time O(n) space
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        open = "{[("
        close = "}])"
        stack = []
        for i in xrange(len(s)):
            if not stack and s[i] in close:
                return False
            if s[i] in open:
                stack.append(s[i])
            else:
                key = stack.pop()
                if key == '{' and s[i] != '}' or key == '[' and s[i] != ']' or key == '(' and s[i] != ')':
                    return False
        return True if not stack else False # notice that if stack is not empty, e.g. "(("
