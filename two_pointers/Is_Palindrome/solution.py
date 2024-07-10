# # Failed at 2 test cases 
# # s = " " and s = "."
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # 1
#         s_lower = s.lower() 
#         # 2
#         s_clean=""
#         for c in s_lower:
#             # check if alphanumeric
#             if self.alphaNum(c):
#                 s_clean+=c

#         ptr_l, ptr_r = 0, len(s_clean) -1 
#         flag = False
#         while ptr_l < ptr_r:
#             if s_clean[ptr_l] != s_clean[ptr_r]:
#                 flag = False
#             else:
#                 flag = True
#             ptr_l +=1
#             ptr_r -=1
#         return flag

#     def alphaNum(self, c):
#         return (ord('A') <= ord(c) <= ord('Z') or 
#                 ord('a') <= ord(c) <= ord('z') or 
#                 ord('0') <= ord(c) <= ord('9'))

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1
        s_lower = s.lower() 
        # 2
        s_alnum = [c for c in s_lower if c.isalnum()]

        return s_alnum == s_alnum[::-1]
"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. 

It is also `case-insensitive` and `ignores all non-alphanumeric characters`.
"""

""" 1st approach -> two failed test cases
1. `case-insensitive` -> lower-case all characters.
2. `ignores all non-alphanumeric characters` -> from lowered-case `s` return alphanumeric characters.
alphanumeric characters -> Include both upper and lower case letters (A to Z, a to z) and numerals (0 to 9)
3. Use two pointers, right and left. 
    Set the left pointer at index 0 and the right pointer at index (len - 1). 
    Check if the value at the left pointer equals the value at the right pointer. 
    If they are equal, increase the left pointer and decrease the right pointer 
    as long as the left pointer is less than the right pointer. 
"""

""" 2nd approach -> accepted.
1. `case-insensitive` -> lower-case all characters.
2. `ignores all non-alphanumeric characters` -> from lowered-case `s` return alphanumeric characters.
alphanumeric characters -> Include both upper and lower case letters (A to Z, a to z) and numerals (0 to 9). 
use `islnum()` python built-in method.
3. Checks if the filtered list resulting from `islnum()` is equal to its reverse. 
"""

# # Trying 1st approach.
# s = "Was it a car or a cat I saw?"
# # 1
# s_lower = s.lower() 
# # 2
# def alphaNum(c):
#     return (ord('A') <= ord(c) <= ord('Z') or 
#             ord('a') <= ord(c) <= ord('z') or 
#             ord('0') <= ord(c) <= ord('9'))

# s_clean=""
# for c in s_lower:
#     # check if alphanumeric
#     if alphaNum(c):
#         s_clean+=c
# # print(s_clean[0])
# ptr_l, ptr_r = 0, len(s_clean) -1 
# flag = False
# while ptr_l < ptr_r:
#     if s_clean[ptr_l] != s_clean[ptr_r]:
#         flag = False
#     else:
#         flag = True
#     ptr_l +=1
#     ptr_r -=1
# print(flag)

# Trying 2nd approach.
# Example 1:
s = "Was it a car or a cat I saw?" # Output: true
sol = Solution()
print(sol.isPalindrome(s))

# Example 2:
s = "tab a cat" # Output: false
print(sol.isPalindrome(s))

# 1st failed test case
s = " " # Output: true
sol = Solution()
print(sol.isPalindrome(s))

# 2nd failed test case
s = "." # Output: true
sol = Solution()
print(sol.isPalindrome(s))
