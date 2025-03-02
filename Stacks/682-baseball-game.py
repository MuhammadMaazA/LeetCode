class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op =="+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(stack[-1]*2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
            
        return sum(stack)

        # Time: O(n) because we are iterating through the list once
        # Space: O(n)  because we are using a stack to store the points