angular.module('myApp', []).controller('myCtrl', function($scope) {
  $scope.elements = []
  for (var i = 0; i < 500; i++) {
    $scope.elements.push(i.toString())
  }
})

setTimeout(() => {
  var debounce = true
  var throttle = true
  var inter = 1


  document.body.onscroll = function() {

    //throttle
    if (throttle) {
      throttle = false
      setTimeout(() => {
        console.log("throttled")
        throttle = true
      }, 200)
    }

    // debounce
    clearTimeout(inter)
    inter = setTimeout(() => {
      debounce = true
    }, 100)
    if (debounce) {
      console.log('Debounced')
      debounce = false
    }
  }
}, 1000)
