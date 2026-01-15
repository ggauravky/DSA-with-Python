#  61. Rotate List (leetcode #61)

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None or k==0:
            return head
        
        l=0
        last = head
        while last.next != None:
            last=last.next
            l+=1
        l+=1
        
        k=k%l
        if k==0:
            return head
        
        current=head
        for _ in range(l-k-1):
            current=current.next
            
        last.next=head
        head=current.next
        current.next=None
        
        return head
    

# 160. Intersection of Two Linked Lists (leetcode #160)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1=headA
        p2=headB
        
        c=0
        
        while True:
            if p1==p2:
                return p1
            
            p1=p1.next
            p2=p2.next
                
            if p2==None:
                p2=headA
                c+=1
            if p1==None:
                p1=headB
            
            if c>1:
                return None