var count=0;
var index=0;
    $.ajax({

        url: 'http://localhost:8888/homepage',
        type: "post",
        success: function (data) {
            successmessage = 'Data was succesfully captured';
           
            for (x in data[2]){
            $("#super").append("</br>"+data[2][x].username+"</br>");


            }

            $('#super').attr('style','text-align:center; color:#7A3E48; font-weight:bold');
            $('#super').css("font-size","100%");



            for (x in data[3]){

              
            $("#party").append("</br>"+data[3][x].username+"</br>");


            }

            $('#party').attr('style','text-align:center; color:#7A3E48; font-weight:bold');
            $('#party').css("font-size","100%");


             for (x in data[4]){

              
            $("#chatty").append("</br>"+data[4][x]._id+"</br>");


            }

            $('#chatty').attr('style','text-align:center; color:#7A3E48; font-weight:bold');
            $('#chatty').css("font-size","110%");



        },
        error: function (data) {
            successmessage = 'Error';
            $("#myAllfriends").text(successmessage);
        },
    });



