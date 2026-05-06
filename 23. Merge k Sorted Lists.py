# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []

        curr = lists

        for list_ in lists:
            arr.append(list_)
        
        tot = []

        for l in arr:
            cur = l
            while cur:
                tot.append(cur.val)
                cur = cur.next
        tot.sort()

        print(tot)

        dummy = ListNode()
        c = dummy

        for num in tot:
            c.next = ListNode(num)
            c = c.next
        return dummy.next
        
