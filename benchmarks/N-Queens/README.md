### **Algorithm and Solving Approach for N-Queens Problem**

The **N-Queens problem** involves placing **N queens** on an **N × N chessboard** such that no two queens threaten each other. This means:
- No two queens should be in the same **row**.
- No two queens should be in the same **column**.
- No two queens should be in the same **diagonal**.


### **Algorithm (Backtracking Approach)**

1. **Start with an empty board**:  
   Create an `N × N` board initialized with `0`, where `0` represents an empty cell and `1` represents a placed queen.

2. **Place queens row by row**:  
   Begin placing queens from **row 0** to **row N-1**.

3. **Check for a safe position**:  
   - Before placing a queen at `board[row][col]`, check if it is **safe** using the `is_safe` function.
   - Ensure no queen is present in the **same column** or **diagonal** (both left and right).

4. **Recursive Backtracking**:
   - If a queen can be placed at `board[row][col]`, mark it as `1`.
   - Recursively call the function for the **next row**.
   - If a valid solution is found (i.e., all queens are placed), store it in the `solutions` list.
   - **Backtrack**: If placing a queen leads to an invalid state, remove it (`board[row][col] = 0`) and try the next column.

5. **Repeat Until All Solutions are Found**:  
   Once all rows are processed, return the list of valid board configurations.


### **Example Execution (N = 4)**
**Solution Output:**
```
Q . . .
. . Q .
. Q . .
. . . Q

. . Q .
Q . . .
. . . Q
. Q . .
```
Each row contains **one queen**, and no two queens attack each other.
