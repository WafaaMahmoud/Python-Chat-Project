from tornado import web, websocket
from pymongo import MongoClient

client = MongoClient()
db = client['pro']
mGroups=[]
groups=[]
groupsState={}

class group(web.RequestHandler):
    def get(self):
        self.render("../templates/group.html")

    def post(self):
        user="doha"
        #user groups
        myGroups=[]
        notingroups=[]
        mGroups = db.user.find({'username':user},{'groups':1,'_id':0})
        for doc in mGroups:
            myGroups=doc['groups']
        print(myGroups)

        #all groups
        groups = db.pgroups.find({},{'name':1,'_id':0})

        #user not in groups
        for document in groups:
            if document['name'] not in myGroups:
                notingroups.append(document['name'])
        print(notingroups)

        groupsState[0]=notingroups
        groupsState[1]=myGroups
        notingroups=[]
        #notingroups=[]
        self.write(groupsState)
