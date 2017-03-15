from tornado import web, websocket
from pymongo import MongoClient

client = MongoClient()
db = client['pro']
mFriends=[]
friends=[]
friendsState={}

class people(web.RequestHandler):
    def get(self):
        self.render("../templates/people.html")

    def post(self):
        user="doha"
        #user friends
        myFriends=[]
        notinfriends=[]
        mFriends = db.user.find({'username':user},{'friends':1,'_id':0})
        for doc in mFriends:
            myFriends=doc['friends']
        print(myFriends)

        #all friends
        friends = db.user.find({},{'username':1,'_id':0})

        #user not in friends
        for document in friends:
            if document['username'] not in myFriends:
                notinfriends.append(document['username'])
        print(notinfriends)

        friendsState[0]=notinfriends
        friendsState[1]=myFriends
        notinfriends=[]
        #notinfriends=[]
        self.write(friendsState)
