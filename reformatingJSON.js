// data given
var response = {
  "UK": [
    {
      "cityName": "london",
      "shortName": "LND",
      "coordinates": {
        "longitude": -0.118,
        "latitude": 51.43534
      }
    },
    {
      "cityName": "Mumbai",
      "shortName": "MUM",
      "coordinates": {
        "longitude": -0.118,
        "latitude": 51.43534
      }
    }
  ],
  "US": [
    {
      "cityName": "New York",
      "coordinates": {
        "longitude": -0.118,
        "latitude": 51.43534
      }
    },
    {
      "cityName": "Patna",
      "shortName": "PAT",
      "coordinates": {
        "longitude": -0.118,
        "latitude": 51.43534
      }
    }
  ]
}

//parse the regions into cities
//skips the key value pairs if data is invalid or empty
// verifies the float values of longitude and latitude
function parseCities(response){
  var result = [];
  if (response){
    

    Object.keys(response).forEach(function(key) {
    var val = response[key];
    for (var i=0; i<val.length;i++){
      console.log()
      var data = {
        "region": key,
        "cityName": val[i].cityName
      }
      if(val[i].shortName != null){
        data.shortName = val[i].shortName;
      }
      if(val[i].coordinates != null){
        if(isFloat(val[i].coordinates.longitude) && isFloat(val[i].coordinates.latitude)){
          data.longitude = val[i].coordinates.longitude; 
          data.latitude = val[i].coordinates.latitude;
        }
        
      }  
      result.push(data);
    }
      //console.log(val);
    ;});
    var final= sortByKey(result, 'cityName');
      return ((final));
  }
}

function isFloat(n){
    return Number(n) === n && n % 1 !== 0;
}

function sortByKey(array, key) {
    return array.sort(function(a, b) {
        var x = a[key]; var y = b[key];
        return ((x < y) ? -1 : ((x > y) ? 1 : 0));
    });
}

console.log (parseCities(response));
