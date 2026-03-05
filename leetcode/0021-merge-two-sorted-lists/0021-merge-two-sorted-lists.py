# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr1=[]
        arr2=[]

        pointer1=list1
        while pointer1 and pointer1.next:
            arr1.append(pointer1.val)
            pointer1=pointer1.next
        if pointer1:
            arr1.append(pointer1.val)

        pointer2=list2
        while pointer2 and pointer2.next:
            arr2.append(pointer2.val)
            pointer2=pointer2.next
        if pointer2:
            arr2.append(pointer2.val)
        
        i=0
        j=0

        ans=[]
        while i < len(arr1) and j< len(arr2):
            if arr1[i]<=arr2[j]:
                ans.append(arr1[i])
                i+=1
            else:
                ans.append(arr2[j])
                j+=1
        ans.extend(arr1[i:])
        ans.extend(arr2[j:])
        
        dummy=ListNode()
        curr=dummy
        for num in ans:
            curr.next=ListNode(num)
            curr=curr.next
        return dummy.next
            

        