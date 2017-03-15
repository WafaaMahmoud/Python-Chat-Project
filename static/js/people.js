var count=0;
var index=0;
    $.ajax({

        url: 'http://localhost:8888/pe',
        type: "post",
        success: function (data) {
            successmessage = 'Data was succesfully captured';
            for (x in data[0]){
                //$("#myAllfriends").append("</br>"+data[1][x].username+"</br>");

            }

            for (x in data[0]){
                $("#myfriends").append("</br>"+data[0][x].friends+"</br>");

            }
            for (x in data[2]){

                if(data[2][x].numberOfColors>count){
                    //console.log(data[2][x].numberOfColors);
                    count=data[2][x].numberOfColors;
                    index=x;
                }


            }

            $("#myAllfriends").append("</br>"+data[2][index].username+"</br>");



        },
        error: function (data) {
            successmessage = 'Error';
            $("#myAllfriends").text(successmessage);
        },
    });



