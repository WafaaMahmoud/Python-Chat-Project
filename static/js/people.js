/**
 * Created by doha on 3/15/17.
 */

$.ajax({
  url:'http://localhost:8888/people',
  type:'post',
  success:function(data){
    myFriends=[]
    notinfriends=[]
    successmessage="data retrieved";
    //console.log(data);
    for(x in data){
      for(y=0;y<data[x].length;y++ ){
        if(x==1){
          $("#myfriends").append("<br/><input type='radio' name='mygroup'>"+data[x][y]+"&nbsp;&nbsp;&nbsp;&nbsp;<button>remove</button></br>");
          myFriends.push(data[x][y])
          console.log(data[x][y])
        }else if(x==0){
          $("#myAllfriends").append("</br><input type='radio' name='groups'>"+data[x][y]+"&nbsp;&nbsp;&nbsp;&nbsp;<button>remove</button></br>");
          notinfriends.push(data[x][y])
          console.log(data[x][y])
        }
        }

    }
  },
  error:function(data){
    console.log("error")
  }

});
