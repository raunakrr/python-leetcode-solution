class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        from collections import defaultdict
        rows=defaultdict(set)
        columns=defaultdict(set)
        squares=defaultdict(set)
        for r in range(9):
            for c in range(9):
                val=board[r][c]
                box=(r//3,c//3)
                if val == ".":
                    continue
                if val in rows[r] or val in columns[c] or val in squares[box]:
                    return False
                
                rows[r].add(val)
                columns[c].add(val)
                squares[box].add(val)
        return True