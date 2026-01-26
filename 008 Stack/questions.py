# 232. Implement Queue using Stacks
# Easy
# Topics
# premium lock icon
# Companies
# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

# Example 1:

# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false
 

# Constraints:

# 1 <= x <= 9
# At most 100 calls will be made to push, pop, peek, and empty.
# All the calls to pop and peek are valid.

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        while(len(self.stack1) > 0):
            self.stack2.append(self.stack1.pop())
            
        self.stack1.append(x)   
        while(len(self.stack2) > 0):
            self.stack1.append(self.stack2.pop())   

    def pop(self) -> int:
        x=self.stack1[-1]
        self.stack1.pop()
        return x

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0



# 20. Valid Parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack

# 844. Backspace String Compare

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            result = []
            for char in string:
                if char != '#':
                    result.append(char)
                elif result:
                    result.pop()
            return ''.join(result)
        
        return build(s) == build(t)
    

# 496. Next Greater Element I
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                smaller_num = stack.pop()
                next_greater[smaller_num] = num
            stack.append(num)
        
        # For elements that have no next greater element
        for num in stack:
            next_greater[num] = -1
        
        return [next_greater[num] for num in nums1]
    
    
    
# 503. Next Greater Element II
class Solution:
    def nextGreaterElements(self, arr: List[int]) -> List[int]:
        arr+=arr
        n=len(arr)
        
        ans=[0]*len(arr)
        stack=[]
        
        for i in range(len(arr)-1,-1,-1):
            while stack and stack[-1]<=arr[i]:
                stack.pop()
            if len(stack)==0:
                ans[i]=-1
            else:
                ans[i]=stack[-1]
            stack.append(arr[i])
            
        return ans[:len(ans)//2]