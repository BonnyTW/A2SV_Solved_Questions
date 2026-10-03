# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        arr = []

        curr = head

        while curr and curr.next:
            arr.append(curr.val)
            curr = curr.next
        
        if curr:
            arr.append(curr.val)
        
        ans = []

        i = 0
        j = len(arr) - 1

        while i < j:
            ans.append(arr[i])
            ans.append(arr[j])

            i += 1
            j -= 1
        
        if len(arr) % 2:
            ans.append(arr[j])
        
        dummy = head
        i = 0

        while dummy:
            dummy.val = ans[i]
            dummy = dummy.next
            i += 1
        
        return head
        
