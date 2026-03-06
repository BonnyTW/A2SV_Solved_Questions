# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        pointer=head

        while pointer and pointer.next:
            arr.append(pointer.val)
            pointer=pointer.next
        
        if pointer:
            arr.append(pointer.val)

        print(arr)

        ans_odd=[]
        ans_even=[]

        for i in range(len(arr)):
            if i%2:
                ans_even.append(arr[i])
            else:
                ans_odd.append(arr[i])
        ans= ans_odd + ans_even
        print(ans)

        dummy=ListNode()
        curr=dummy
        for num in ans:
            curr.next=ListNode(num)
            curr=curr.next
        return dummy.next