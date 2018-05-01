class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] arr = new int[cost.length+1];
        arr[0] = cost[0];
        arr[1] = cost[1];
        int res = 0;
        for(int i=2; i<=cost.length; i++){
            if(i==cost.length){
                res = Math.min(arr[i-1], arr[i-2]);
            }
            else{
                arr[i] = Math.min(arr[i-1], arr[i-2]) + cost[i];
            }
            
        }
        return res;
    }
}
