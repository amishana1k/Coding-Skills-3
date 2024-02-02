class MyStack:
    def __init__(self):
        self.q = deque()
    def push(self, x: int) -> None:
        return self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]
        

    def empty(self) -> bool:
        return len(self.q)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
#q = deque([1, 2, 3, 4, 5])

# stack_instance.pop()
# The pop method will execute the following steps:

# Loop Iteration:

# In the first iteration of the loop, i will be 0.
# Inside the loop, self.q.append(self.q.popleft()) will move the leftmost element (1) to the right end of the deque. After this operation, the deque becomes [2, 3, 4, 5, 1].
# The loop continues until i reaches len(self.q) - 1, which means it will iterate 4 times in total.
# After Loop:

# After the loop, all elements except the last one (1) are moved to the right end of the deque. The deque now looks like this: [2, 3, 4, 5, 1].
# Popping the Last Element:

# Finally, return self.q.popleft() removes and returns the last element of the deque, which is 1.
# The resulting deque becomes [2, 3, 4, 5].
# So, after executing the pop method, the top element (5) is removed from the stack, and the stack now contains [2, 3, 4].
