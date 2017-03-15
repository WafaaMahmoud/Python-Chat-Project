from tornado import web,websocket
import pymongo



class signup(web.RequestHandler):
	def get(self):
		self.render("../templates/Loginpage.html")
	def post(self):
		client=pymongo.MongoClient()
		db=client.pro
		uname=self.get_argument("username")
		pwd=self.get_argument("pwd")
		email=self.get_argument("email")
		db.user.insert({"username":uname,"password":pwd,"email":email})