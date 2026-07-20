# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 2:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            digit = total % 10
            carry = total // 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next 

        return dummy.next


# Convert Python list to linked list
def createLinkedList(values):

    dummy = ListNode(0)
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next

# Print linked list
def printLinkedList(head):

    values = []

    while head:
        values.append(head.val)
        head = head.next

    print(values)


solution = Solution()

# Test Case 1
l1 = createLinkedList([0])
l2 = createLinkedList([0])

testCase1 = solution.addTwoNumbers(l1, l2)

print("Test Case 1:")
printLinkedList(testCase1)


# Test Case 2
l1 = createLinkedList([9, 9, 9, 9, 9, 9, 9])
l2 = createLinkedList([9, 9, 9, 9])

testCase2 = solution.addTwoNumbers(l1, l2)

print("Test Case 2:")
printLinkedList(testCase2)


