from tornado import web,websocket
import pymongo
#import Cookie

clients = []
usname={}
pr = []
msg = []
class WSHandler(websocket.WebSocketHandler):
	owner= None
	def open(self):
		clients.append(self)
		

	def on_message(self,message):
		print("open a soket")
		owner=self.get_secure_cookie("uname")
		print(self.get_secure_cookie("uname").decode("utf-8"))
		for c in clients:
			c.write_message(owner.decode("utf-8") +": "+message)

		
			
class ChatHandler(web.RequestHandler):
	def get(self):
		self.render("../templates/groupchat.html")

class Login(web.RequestHandler):
	def get(self):
		self.render("../templates/Loginpage.html")
		
	"""docstring for Login"""
	def post(self):
		
		client=pymongo.MongoClient()
		db=client.pro
		pr=db.user.find()
		uname=self.get_argument("username")
		pwd=self.get_argument("pwd")
		self.set_secure_cookie("uname", uname)
		print(uname)
		
		#c = Cookie.SimpleCookie()
		for p in pr:
			#print(p["username"])
			if (uname == p["username"]) and (int(pwd) == p["password"]):
				
				print("sucessfully login")
				self.redirect("/chat")
				
				#self.set_cookie("username",uname)
			else:
				print("not valid Email password")
		
