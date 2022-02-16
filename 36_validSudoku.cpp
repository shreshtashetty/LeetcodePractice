// 36. Valid Sudoku

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_map<int,int>> rows;
        vector<unordered_map<int,int>> cols;
        vector<unordered_map<int,int>> boxes;
        
        for(int i=0;i<9;i++){
            unordered_map<int,int> map;
            rows.push_back(map);
            cols.push_back(map);
            boxes.push_back(map);
        }
        
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                auto num = board[i][j];
                
                if(num!='.'){
                    int n = num-'0';
                    int box_index = (i / 3 ) * 3 + j / 3;
 
                    rows[i][n] = rows[i][n]+1;
                    cols[j][n] = cols[j][n]+1;
                    boxes[box_index][n] = boxes[box_index][n]+1;
                    
                    if(rows[i][n]>1 || cols[j][n]>1 || boxes[box_index][n]>1)
                        return false;
                }                
            }
        }
        
        return true;
    }
};
