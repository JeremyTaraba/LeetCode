import java.nio.charset.Charset;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Valid_Sudoku {
    public static void main(String[] args) {
        char[][] board = new char[1][1];


        Map<Integer, HashSet<Character>> rows = new HashMap<Integer, HashSet<Character>>();
        Map<Integer, HashSet<Character>> column = new HashMap<Integer, HashSet<Character>>();
        Map<String, HashSet<Character>> boxes = new HashMap<String, HashSet<Character>>();


        for(int r = 0; r < board.length; r++){
            for(int c = 0; c < board[c].length; c++){
                String box = String.format("%i,%i", r/3,c/3);
                // Java wants you to check if the row exists first so cant use get unless check if null first
                // would need to separate these loops and don't feel like rewriting it so new solution is at bottom
                if(rows.get(r).contains(board[r][c]) || column.get(c).contains(board[r][c]) || boxes.get(box).contains(board[r][c])){
                    return false;
                }   
                HashSet<Character> temp = rows.get(r);
                temp.add(board[r][c]);
                rows.put(Integer.valueOf(r), temp);

                temp = column.get(c);
                temp.add(board[r][c]);
                column.put(Integer.valueOf(c), temp);

                temp = boxes.get(box);
                temp.add(board[r][c]);
                boxes.put(box, temp);


            }
        }
    }

        

// Solution using only 1 hashset and using strings to add them to the set
public boolean isValidSudoku(char[][] board) {
    Set<String> seen = new HashSet<>();
    for (int i=0; i<9; ++i) {
        for (int j=0; j<9; ++j) {
            char number = board[i][j];
            if (number != '.')
                if (!seen.add(number + " in row " + i) || !seen.add(number + " in column " + j) || !seen.add(number + " in block " + i/3 + "-" + j/3))
                    return false;
        }
    }
    return true;
}

}
