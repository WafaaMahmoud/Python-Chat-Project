from tornado import web,ioloop
from handlers.ajax import APIHandler
from handlers.sse import EventHandler,SSEHandler
from handlers.login import ChatHandler,WSHandler,Login
from handlers.people import people
from handlers.signup import signup
from handlers.group import group
from handlers.homepage import homepage


class MainHandler(web.RequestHandler):
    def get(self):
        self.render("templates/homepage.html")

app = web.Application([
	(r"/", MainHandler),
        (r"/myapi", APIHandler),
        (r"/sse", SSEHandler),
        (r"/event", EventHandler),
        (r"/chat", ChatHandler),
        (r"/log", Login),
        (r"/signup", signup),
        (r"/people", people),
        (r"/group", group),
        #("/homepage", homepage),
        (r"/ws", WSHandler)
	],static_path='static',debug=True,cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__")

app.listen(8888)
ioloop.IOLoop.current().start()
