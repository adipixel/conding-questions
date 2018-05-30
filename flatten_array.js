var arr = [1,2,3,[1,2,3,4, [2,3,4]]];

function flattenRecursive(arr){
	var res = arr.reduce((acc, val)=>{
  	if(Array.isArray(val)){
    	return acc.concat(flattenRecursive(val))
    }
    else{
    	return acc.concat([val])
    }
  }, [])
  
	return res
}

function flattenIterative(arr) {
  var array = [];
  while(arr.length) {
    var value = arr.shift();
    if(Array.isArray(value)) {
      // this line preserve the order
      arr = value.concat(arr);
    } else {
      array.push(value);
    }
  }
  return array;
}

console.log(flattenRecursive(arr))
console.log(flattenIterative(arr))
