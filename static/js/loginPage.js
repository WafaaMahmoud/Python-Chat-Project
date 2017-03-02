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