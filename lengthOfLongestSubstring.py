# Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:

    def lengthOfLongestSubstring(self, s):

        seen = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):

            if char in seen and seen[char] >= left:
                left = seen[char] + 1

            seen[char] = right

            max_length = max(max_length, right - left + 1)

        return max_length
    
solution = Solution()

# Test Case

print("Test Case 1 : ", solution.lengthOfLongestSubstring("abcabcbb"))
print("Test Case 2 : ", solution.lengthOfLongestSubstring("bbbbb"))
print("Test Case 3 : ", solution.lengthOfLongestSubstring("pwwkew"))