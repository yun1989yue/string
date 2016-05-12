'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses. 

For example, given n = 3, a solution set is: 

"((()))", "(()())", "(())()", "()(())", "()()()" 
'''
"""
M1: recursion
"""
class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n, openings = 0): # openings means how many "(" haven't been paired
        if n == 0: # no more available "("
            return [')'*openings]
        if openings == 0: # need more "("
            return ['(' + x for x in self.generateParenthesis(n-1,1)]
        else:
            return ['(' + x for x in self.generateParenthesis(n-1,openings+1)] + [')' + x for x in self.generateParenthesis(n,openings-1)]
