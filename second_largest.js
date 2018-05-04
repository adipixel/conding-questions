/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Complete the function
    var lar = Number.MIN_SAFE_INTEGER;
    var secLar = Number.MIN_SAFE_INTEGER;
    nums.forEach((num)=>{
        if(num>lar){
            secLar = lar;
            lar = num;
            
        }
        else{
            if(num > secLar && num != lar){
                secLar = num;
            }
        }
    });
    return secLar;
}
