from tornado import web,websocket
import pymongo

clients = []
pr = []
msg = []
class WSHandler(websocket.WebSocketHandler):
	def open(self):
		clients.append(self)
		

	def on_message(self,message):
		client=pymongo.MongoClient()
		db=client.pro
		pr=db.user.find()
		print(message)
		msg=message.split(":")
		print(msg[1])
		print(pr)
		
		#print(pr["name"])
		for p in pr:
			if (msg[0] == p["username"]) and (int(msg[1]) == p["password"]):
				print("in for")
				self.write_message("successfuly login")
				db.user.update({"username":msg[0]},{ "$set":{"is_active":"true"}})
				print("successfuly login")
				#self.render("../templates/people.html")
				#for c in clients:u
				#	c.write_message(p["name"]+" it is in the databse")
			else:
				self.write_message("not valid id or password")
			
class ChatHandler(web.RequestHandler):
	def get(self):
		self.render("../templates/chat.html")

class Login(web.RequestHandler):
	"""docstring for Login"""
	def get(self):
		self.render("../templates/Loginpage.html")
