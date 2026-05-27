public class Solution {
    public bool IsValidSudoku(char[][] board) {
        // box:
		// 	0, 0: 1, 2, 3 ...
		// 	0, 1: 1, 2, 3 ...
		
		// horizontal
		// vertical
		
		var box = new Dictionary<ValueTuple<int, int>, HashSet<char>>();
		var hor = new Dictionary<int, HashSet<char>>();
		var vert = new Dictionary<int, HashSet<char>>();
		
		for (int i = 0; i < board.Length; i++) {
			for (int j = 0; j < board[0].Length; j++) {
				if (board[i][j] == '.') {
					continue;
				}
	
				// First time encountering key
                if (!hor.ContainsKey(i)) hor[i] = new HashSet<char>();
                if (!vert.ContainsKey(j)) vert[j] = new HashSet<char>();
                if (!box.ContainsKey((i / 3, j / 3))) box[(i / 3, j / 3)] = new HashSet<char>();
			
				// Add returns False if the value is already in the Set	
				if (!box[(i / 3, j / 3)].Add(board[i][j]) ||
					!hor[i].Add(board[i][j]) ||
					!vert[j].Add(board[i][j])) {
					return false;
				}
			}
		}
		return true;
    }
}
