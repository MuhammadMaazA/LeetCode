from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # Direction mapping: 1-Right, 2-Left, 3-Down, 4-Up
        direction = {
            1: [0, 1],   # Right
            2: [0, -1],  # Left
            3: [1, 0],   # Down
            4: [-1, 0]   # Up
        }

        ROWS, COLS = len(grid), len(grid[0])

        q = deque([(0, 0, 0)])  # (row, col, cost)
        min_cost = {(0, 0): 0}   # (row, col): min_cost

        while q:
            r, c, cost = q.popleft()
            
            # If we've reached the destination, return the cost
            if (r, c) == (ROWS - 1, COLS - 1):
                return cost

            for d in direction:
                dr, dc = direction[d]  # Corrected assignment
                nr, nc = r + dr, c + dc
                n_cost = cost if d == grid[r][c] else cost + 1

                # Check boundaries
                if not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue

                # If the new cost is better, update and add to the queue
                if n_cost < min_cost.get((nr, nc), float("inf")):
                    min_cost[(nr, nc)] = n_cost
                    if d == grid[r][c]:
                        q.appendleft((nr, nc, n_cost))  # No additional cost
                    else:
                        q.append((nr, nc, n_cost))      # Additional cost incurred

        # If the destination is unreachable, return -1
        return -1
