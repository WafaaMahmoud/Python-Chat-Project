from tornado import web,ioloop
from handlers.ajax import APIHandler
from handlers.sse import EventHandler,SSEHandler
from handlers.login import ChatHandler,WSHandler,Login


class MainHandler(web.RequestHandler):
    def get(self):
        self.render("templates/chat.html")

app = web.Application([
	(r"/", MainHandler),
        (r"/myapi", APIHandler),
        (r"/sse", SSEHandler),
        (r"/event", EventHandler),
        (r"/chat", ChatHandler),
        (r"/log", Login),
        (r"/ws", WSHandler)
	],static_path='static',debug=True)

app.listen(8888)
ioloop.IOLoop.current().start()
