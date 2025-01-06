class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        # Left to Right Pass
        count = 0    # Number of balls encountered so far
        operations = 0  # Total operations to move balls to current box

        for i in range(n):
            answer[i] += operations
            if boxes[i] == '1':
                count += 1
            operations += count

        # Right to Left Pass
        count = 0    # Number of balls encountered so far from the right
        operations = 0  # Total operations to move balls to current box

        for i in range(n-1, -1, -1):
            answer[i] += operations
            if boxes[i] == '1':
                count += 1
            operations += count

        return answer
