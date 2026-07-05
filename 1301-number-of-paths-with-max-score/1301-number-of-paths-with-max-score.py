class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        MOD = 1_000_000_007
        n = len(board)
        
        # Initialize DP tables
        dp_score = [[-1] * n for _ in range(n)]
        dp_count = [[0] * n for _ in range(n)]
        
        # Base case setup
        dp_score[n-1][n-1] = 0
        dp_count[n-1][n-1] = 1
        
        # Process grid backwards from bottom-right to top-left
        for r in reversed(range(n)):
            for c in reversed(range(n)):
                # FIXED: Only skip obstacles. Let 'S' execute so its neighbors can read from it.
                if board[r][c] == 'X': 
                    continue
                    
                best_score = -1
                paths = 0
                
                # Check bottom, right, and bottom-right neighbors
                for dr, dc in [(1, 0), (0, 1), (1, 1)]:
                    nr, nc = r + dr, c + dc
                    if nr < n and nc < n and dp_score[nr][nc] != -1:
                        if dp_score[nr][nc] > best_score:
                            best_score = dp_score[nr][nc]
                            paths = dp_count[nr][nc]
                        elif dp_score[nr][nc] == best_score:
                            paths = (paths + dp_count[nr][nc]) % MOD
                
                # Update current cell if a valid path exists from a neighbor
                if best_score != -1:
                    # Ignore 'E' and 'S' character numeric conversions
                    current_val = int(board[r][c]) if board[r][c] not in ('E', 'S') else 0
                    dp_score[r][c] = best_score + current_val
                    dp_count[r][c] = paths

        # Result verification at target 'E' (0,0)
        if dp_score[0][0] == -1:
            return [0, 0]
        return [dp_score[0][0], dp_count[0][0]]
