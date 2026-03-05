# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr=[]
        pointer = head

        while pointer and pointer.next:
            arr.append(pointer.val)
            pointer=pointer.next
        if pointer:
            arr.append(pointer.val) 
        return arr==arr[::-1]
        