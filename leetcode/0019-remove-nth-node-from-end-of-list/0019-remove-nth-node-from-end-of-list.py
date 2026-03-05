# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head_len=1
        pointer=head

        while pointer and pointer.next:
            head_len+=1
            pointer=pointer.next
        print(head_len)

        index=head_len - n 

        if index==0:
            return head.next

        pointer2= prev = head

        while pointer2 and index>0:
            index-=1
            prev=pointer2
            pointer2=pointer2.next
        prev.next=pointer2.next

        return head
        
        