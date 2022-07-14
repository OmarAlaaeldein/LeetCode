class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        // O(1) space solution
        // O(m)+O(n)+O(mn)+O(mn)+O(m)+O(n)=O(mn) time solution
        int rows=matrix.size(); // n
        int cols=matrix[0].size(); // m
        int row0=0; // indicator to save the status of row0
        int col0=0; // indicator to save the status of col0
        for (int i=0;i<cols;i++){
            if (matrix[0][i]==0){
                row0=1; // row will be zeroed after completing inner part
                break;
            }
        }
        for (int i=0;i<rows;i++){
            if (matrix[i][0]==0){
                col0=1; // col will be zeroed after completing inner part
                break;
            }
        }
        
        for (int i=1;i<rows;i++){ // set a dummy index array in 0th row, column
            for (int j=1;j<cols;j++){
                if (matrix[i][j]==0){
                    matrix[i][0]=0;
                    matrix[0][j]=0;
                }
            }
        }
        // inner part
        for (int i=1;i<rows;i++){ // zero stuff
            for (int j=1;j<cols;j++){
                if (matrix[i][0]==0 or matrix[0][j]==0){
                    matrix[i][j]=0;
                }
            }
        }
        if (row0==1){
            for (int i=0;i<cols;i++){
                matrix[0][i]=0;
            }
        }
        if (col0==1){
            for (int i=0;i<rows;i++){
                matrix[i][0]=0;
            }
        }
    }
};