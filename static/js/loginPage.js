//$(function(){
//	webSocket= new WebSocket("ws://localhost:8888/ws");
//	webSocket.onmessage = function(e){
//		var msg=e.data;
//		console.log(msg);
		//if(msg==="no")
//		$("#error").append("<p>"+msg+"</p>");
		//else
		//	$("#error").append("<p>successful login"+msg+"</p>");
//	}
	// webSocket.onclose = function(e){
	// 	// console.log(e);
	// }
//	$('#log').click(function(e){
//		var msg = $("#username").val()+":"+$("#pwd").val()
//		webSocket.send(msg)
		//$("#message").val('')
//	})
//})


$('input[type="submit"]').mousedown(function(){
  $(this).css('background', '#963c9b');
});
$('input[type="submit"]').mouseup(function(){
  $(this).css('background', '#963c9b');
});

$('#loginform').click(function(){
  $('.login').fadeToggle('slow');
  $(this).toggleClass('green');
});

$('#Register').click(function(){
  $('.Signup').fadeToggle('slow');
  $(this).toggleClass('green');
});



$(document).mouseup(function (e)
{
    var container = $(".login");

    if (!container.is(e.target) // if the target of the click isn't the container...
        && container.has(e.target).length === 0) // ... nor a descendant of the container
    {
        container.hide();
        $('#loginform').removeClass('green');
    }

 var container2 = $(".Signup");

    if (!container2.is(e.target) // if the target of the click isn't the container...
        && container2.has(e.target).length === 0) // ... nor a descendant of the container
    {
        container2.hide();
        $('#Register').removeClass('green');
    }

});