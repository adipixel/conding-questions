var arr = [1,2,3,[1,2,3,4, [2,3,4]]];

function flatten(arr){
	var res = arr.reduce((acc, val)=>{
  	if(Array.isArray(val)){
    	return acc.concat(flatten(val))
    }
    else{
    	return acc.concat([val])
    }
  }, [])
  
	return res
}


console.log(flatten(arr))
