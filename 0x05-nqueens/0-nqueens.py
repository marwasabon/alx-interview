#!/usr/bin/python3
"""Solves the N-queens puzzle.
"""
import sys


def solve_n_queens(n):  
    def backtrack(row, columns, diagonals1, diagonals2):  
        if row == n:  
            result.append(solution[:])  
            return  
        
        for col in range(n):  
            if columns[col] or diagonals1[row - col + n] or diagonals2[row + col]:  
                continue  
            
            # place the queen  
            solution[row] = col  
            columns[col] = diagonals1[row - col + n] = diagonals2[row + col] = True  
            
            # move to the next row  
            backtrack(row + 1, columns, diagonals1, diagonals2)  
            
            # remove the queen (backtrack)  
            columns[col] = diagonals1[row - col + n] = diagonals2[row + col] = False  
    
    result = []  
    columns = [False] * n  
    diagonals1 = [False] * (2 * n)  
    diagonals2 = [False] * (2 * n)  
    solution = [-1] * n  
    backtrack(0, columns, diagonals1, diagonals2)  
    return result  

 
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    if len(sys.argv) != 2:  
        print("Usage: nqueens N")  
        sys.exit(1)  
    
    if not sys.argv[1].isdigit():  
        print("N must be a number")  
        sys.exit(1)  
    
    n = int(sys.argv[1])  
    
    if n < 4:  
        print("N must be at least 4")  
        sys.exit(1)  

    solutions = solve_n_queens(n)  
    for sol in solutions:  
        print([[r, c] for r, c in enumerate(sol)])
