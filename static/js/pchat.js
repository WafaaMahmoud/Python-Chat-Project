/**
 * Created by doha on 3/16/17.
 */
var webSocket;
//var name=document.cookie;
//console.log(document.cookie.uname);
$(function(){



	webSocket= new WebSocket("ws://localhost:8888/pchat");
	// webSocket.onopen = function(e){
	// 	//var msg = {code:0,uid:$("#group-id").val()}
	// 	this.send()
    //
	// }
	webSocket.onmessage = function(e){
		console.log(e.data)
		$("#chatContent").append("</br>"+e.data+"</br>")
	}

	webSocket.onclose = function(e){
		 console.log(e);
	}

	$('#send').click(function(e){
		var msg = $("#chatInput").val()
        //var to = self.get
		webSocket.send(msg)
		$("#chatInput").val('')
	})
})

//function startChat(){
//	name = $("#userName").val();

//}//
