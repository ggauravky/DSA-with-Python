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

# 2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=head1
        curr2=head2
        
        ans=ListNode(-1)
        c=0
        curr3=ans
        
        while curr1!=None or curr2!=None:
            total=c
            c=0
            
            if curr1!=None:
                total+=curr1.val
                curr1=curr1.next
            if curr2!=None:
                total+=curr2.val
                curr2=curr2.next
            
            if total>9:
                c=1
                total-=10
            
            newNode=ListNode(total)
            curr3.next=newNode
            curr3=curr3.next
            
        if c>0:
            newNode=ListNode(c)
            curr3.next=newNode
            
        return ans.next