# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        arr1=[]
        arr2=[]

        p1=list1

        while p1 and p1.next:
            arr1.append(p1.val)
            p1=p1.next
        if p1:
            arr1.append(p1.val)
        
        print(arr1)

        p2=list2

        while p2 and p2.next:
            arr2.append(p2.val)
            p2=p2.next
        if p2:
            arr2.append(p2.val)
        print(arr2)

        i,j=0,0
        res=[]
        while i<len(arr1) and j< len(arr2):
            if arr1[i]<=arr2[j]:
                res.append(arr1[i])
                i+=1
            else:
                res.append(arr2[j])
                j+=1
        res.extend(arr1[i:])
        res.extend(arr2[j:])
        
        dummy=ListNode()
        curr=dummy

        for num in res:
            curr.next=ListNode(num)
            curr=curr.next
        return dummy.next

            

        