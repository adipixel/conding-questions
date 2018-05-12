# Javascript Prototype Demonstration

const Food = function(){};
Food.prototype.eat = function(){
	return('I ate food');
}

var Apple = function(){};

Apple.prototype = new Food();

Apple.prototype.taste = function(){
  return('Apple is sweet')
}

Apple.prototype.eat = function(){
  return('I ate an apple')
}

var apple = new Apple();
console.log(apple.eat())
console.log(apple.taste())
