# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):

        # Always perform binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:

            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1

            if partition1 == 0:
                max_left1 = float('-inf')
            else:
                max_left1 = nums1[partition1 - 1]

            if partition1 == m:
                min_right1 = float('inf')
            else:
                min_right1 = nums1[partition1]

            if partition2 == 0:
                max_left2 = float('-inf')
            else:
                max_left2 = nums2[partition2 - 1]

            if partition2 == n:
                min_right2 = float('inf')
            else:
                min_right2 = nums2[partition2]

            # Correct partition
            if max_left1 <= min_right2 and max_left2 <= min_right1:

                # Even number of elements
                if (m + n) % 2 == 0:
                    return (
                        max(max_left1, max_left2)
                        + min(min_right1, min_right2)
                    ) / 2

                # Odd number of elements
                else:
                    return max(max_left1, max_left2)

            elif max_left1 > min_right2:
                right = partition1 - 1

            else:
                left = partition1 + 1

solution = Solution()
print(solution.findMedianSortedArrays([1,3], [2]))
print(solution.findMedianSortedArrays([1,2], [3,4]))