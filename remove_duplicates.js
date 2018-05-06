/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    var ptr = 1
    var rpr = 1
    while(ptr < nums.length){
        
        if(nums[ptr] == nums[ptr-1]){
            while( ptr<nums.length && nums[ptr] == nums[ptr-1]){
                ptr +=1
            }
            if(ptr>=nums.length){
                break
            }
        }
        nums[rpr]=nums[ptr]
            rpr +=1
            ptr +=1
    }
    nums.length = rpr
    //console.log(nums)
    
};
