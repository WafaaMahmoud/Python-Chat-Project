from tornado import web,ioloop
from handlers.ajax import APIHandler

class MainHandler(web.RequestHandler):
    def get(self):
        self.render("templates/index.html")

app = web.Application([
		(r"/", MainHandler),
        (r"/myapi", APIHandler)
	],static_path='static',debug=True)

app.listen(8888)
ioloop.IOLoop.current().start()
