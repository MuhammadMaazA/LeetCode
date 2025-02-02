class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create 9 sets for rows, columns, and sub-boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Loop through every cell in the board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue # Skip empty cells

                # Calculate box integer using integer division
                box_index = (i//3) *3 + (j//3) # Determines which of the 9 sub-boxes the current cell belongs to

                # Check if the current number is already seen in hte corresposding row, column, or box
                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False
                
                # Add the current number to the corresponding row, column, and box sets
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)
        return True