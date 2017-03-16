from tornado import web, websocket
import pymongo

# import Cookie

clients = []
dusname = {}
pr = []
msg = []
no_users=0
no_groups=0
max_group=20
groups_member={}


class WSHandlerP(websocket.WebSocketHandler):
    owner = None
    def get(self):
        pass

    def open(self):
        global no_users
        dusname[no_users] = self.get_secure_cookie("uname").decode("utf-8")
        self.uname = self.get_secure_cookie("uname").decode("utf-8")
        ##############self.to de mafrood t5od qema el to
        self.to= self.get_query_arguments("to")
        no_users += 1
        clients.append(self)



    def on_message(self, message):
        for c in clients:
            print("ya rab")
            if(c.uname==c.to):
                c.write_message(message)

class WSHandler(websocket.WebSocketHandler):
    owner = None

    def open(self):
        global no_users
        dusname[no_users] = self.get_secure_cookie("uname").decode("utf-8")
        self.uname=self.get_secure_cookie("uname").decode("utf-8")
        no_users += 1
        clients.append(self)

    def on_message(self, message):
        print("open a soket")
        owner = self.get_secure_cookie("uname")
        print(self.get_secure_cookie("uname").decode("utf-8"))
        print(dusname)

        for c in clients:
            #if(c.name==to) where you want to make a private chat
            if(c.name in groups_member[self.get_query_arguments("id")]):
                 for c.uname in groups_member[self.get_query_arguments("id")]:
                    c.write_message(owner.decode("utf-8") + ": " + message)


class ChatHandler(web.RequestHandler):
    def get(self):
        self.render("../templates/peoplechat.html")


class gChatHandler(web.RequestHandler):
    def get(self):
        user = self.get_secure_cookie("uname").decode("utf-8")

        gid= self.get_query_arguments("id");
        print(gid[0])
        global no_groups
        client = pymongo.MongoClient()
        db = client.pro
        myGroups = []
        notingroups = []
        mGroups =  db.pgroups.find({"name":gid[0]},{'member':1,'_id':0})
        for doc in mGroups:
            myGroups=doc['member']
        print(myGroups)
        groups_member[gid[0]]=myGroups
        print( groups_member)
        no_groups +=1
        self.render("../templates/groupchat.html",gid=gid)
    def post(self):
        pass
        #gid = self.get_body_arguments("id");
        #self.render("../templates/groupchat.html")
        #self.write(gid[0])




class Login(web.RequestHandler):
    def get(self):
        self.render("../templates/Loginpage.html")

    """docstring for Login"""

    def post(self):

        client = pymongo.MongoClient()
        db = client.pro
        pr = db.user.find()
        uname = self.get_argument("username")
        pwd = self.get_argument("pwd")
        self.set_secure_cookie("uname", uname)
        print(uname)

        # c = Cookie.SimpleCookie()
        for p in pr:
            # print(p["username"])
            if (uname == p["username"]) and (int(pwd) == p["password"]):

                print("sucessfully login")
                self.redirect("/chat")

            # self.set_cookie("username",uname)
            else:
                print("not valid Email password")
