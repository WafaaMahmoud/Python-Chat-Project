var count=0;
var index=0;
    $.ajax({

        url: 'http://localhost:8888/homepage',
        type: "post",
        success: function (data) {
            successmessage = 'Data was succesfully captured';
           
            for (x in data[2]){

                if(data[2][x].numberOfColors>count){
                    //console.log(data[2][x].numberOfColors);
                    count=data[2][x].numberOfColors;
                    index=x;
                }


            }

            $("#party").append("</br>"+data[2][index].username+"</br>");
            $('#party').attr('style','text-align:center; color:#7A3E48; font-weight:bold');
            $('#party').css("font-size","150%");



        },
        error: function (data) {
            successmessage = 'Error';
            $("#myAllfriends").text(successmessage);
        },
    });



