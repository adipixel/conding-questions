class MyStack{
	constructor(){
  	this.stack = []
    this.minStack = [0]
  }
  
  peek(){
  	return this.stack[(this.stack.length)-1]
  }
  
  push(e){
  	this.stack.push(e)
    if(e < this.stack[this.minStack[this.minStack.length-1]]){
    	this.minStack.push((this.stack.length)-1)
    }
  }
  
  pop(){
  	let slen= this.stack.length-1
  	let popedItem = this.stack.pop()
    if(slen == this.minStack[this.minStack.length-1]){
    	this.minStack.pop()
    }
    return popedItem
  }
  
  peekMin(){
  	return this.stack[this.minStack[(this.minStack.length)-1]]
  }
}


let ms = new MyStack()
ms.push(5)
ms.push(1)
ms.push(2)
ms.push(0)

console.log(ms.peek())
console.log(ms.peekMin())
console.log(ms.pop())
console.log(ms.peekMin())
