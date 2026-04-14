class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        //Check each row
        for(int row = 0; row < 9; row++){
            unordered_set<char> checked;
            for(int i = 0; i < 9; i++){
                if(board[row][i] == '.'){
                continue;
                }
                if(checked.count(board[row][i]) > 0){
                    return false;
                }
                checked.insert(board[row][i]);
            }
        }

        //Check each column
        for(int col = 0; col < 9; col++){
            unordered_set<char> checked;
            for(int i = 0; i < 9; i++){
                if(board[i][col] == '.'){
                continue;
                }
                if(checked.count(board[i][col]) > 0){
                    return false;
                }
                checked.insert(board[i][col]);
            }
        }

        //Check each 3x3 box
        for(int square = 0; square < 9; square++){
            unordered_set<char> checked;
            for(int i = 0; i < 3; i++){
                for(int j =0; j < 3; j++){
                    int row = (square / 3) * 3 + i;
                    int col = (square % 3) * 3 + j;
                    if(board[row][col] == '.'){
                        continue;
                    }
                    if(checked.count(board[row][col])){
                        return false;
                    }
                    checked.insert(board[row][col]);
                }
            }
        }
        return true;
    }
};
