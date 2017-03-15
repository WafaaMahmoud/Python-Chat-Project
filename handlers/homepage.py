from tornado import web, websocket
from pymongo import MongoClient

client = MongoClient()
db = client['pro']
jfile={}
fs={}
doha={}
max_f={}

class homepage(web.RequestHandler):

    def get(self):
        self.render("../templates/homepage.html")
    def post(self):
            count1 = 0
            count2=0
            count3=0
            cursor = db.user.find({},{'username':1,'_id':0})
            for document in cursor:
                #print(document)
                jfile[count1]=document
                count1 +=1
            cursor1 = db.user.find({},{'friends':1,'_id':0})
            for doc in cursor1:
                #print(doc)
                fs[count2]=doc
                count2 +=1
            doha[0]=fs
            doha[1]=jfile
            
            max_fr = db.user.aggregate([{"$project": {"username": 1,"_id":0 ,"numberOfColors": { "$size": "$friends"}}}])
            for doc in max_fr:
                print(doc)
                max_f[count3]=doc
                count3 +=1
            doha[0] = fs
            doha[1] = jfile
            doha[2]=max_f


            self.write(doha);


            print(doha)

