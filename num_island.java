https://leetcode.com/problems/number-of-islands/description/

class Solution {
    public int numIslands(char[][] grid) {
        int islandCounter = 0;
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[0].length; j++){
                //System.out.print(grid[i][j]);
                if(grid[i][j] == '1'){
                    grid[i][j] = '2';
                    findNeighbours(i, j, grid);
                    
                    islandCounter += 1;
                }
            }
             //System.out.println();
        }
        return islandCounter;
    }
    
    public void findNeighbours(int i, int j, char[][] grid){
        if(j>0 && grid[i][j-1] == '1'){
            grid[i][j-1] = '2';
            findNeighbours(i, j-1, grid);
        }
        if(j<grid[0].length-1 && grid[i][j+1] == '1'){
            grid[i][j+1] = '2';
            findNeighbours(i, j+1, grid);
        }
        if(i<grid.length-1 && grid[i+1][j] == '1'){
            grid[i+1][j] = '2';
            findNeighbours(i+1, j, grid);
        }
        if(i>0 && grid[i-1][j] == '1'){
            grid[i-1][j] = '2';
            findNeighbours(i-1, j, grid);
        }
        
    }
}
