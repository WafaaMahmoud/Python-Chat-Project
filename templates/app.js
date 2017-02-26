//Open Weather Api Link
var url = "http://api.openweathermap.org/data/2.5/weather?q=Paris,uk&appid=feaecb4e28deb1be3144c667e8463d2a";
//Google Maps Api Src Link
// var googleMap = "http://maps.googleapis.com/maps/api/staticmap?center="+lang+","+lat+"&zoom=14&size=400x300&sensor=false";

function receiveData(){
	$.ajax({
	method: "get",
	async: true,
	url: url,
	success: function(res){
	console.log(res);
	console.log(res.weather[0].main);
	//setTimeout(receiveData,5000);
	}
	})
}
receiveData()

