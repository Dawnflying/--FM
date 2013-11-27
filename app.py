import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
         self.render("index.html", title="My title")
        
        
class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html", title="Login")
 
class RegisterHandler(tornado.web.RequestHandler):
     def get(self):
         self.render("register.html", title="Register")
 
 
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/login", LoginHandler),
            (r"/register", RegisterHandler),
#             (r"/auth/logout", AuthLogoutHandler),
#             (r"/a/message/new", MessageNewHandler),
#             (r"/a/message/updates", MessageUpdatesHandler),
        ]
        settings = dict(
            debug=True,
#             cookie_secret="43oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
#             login_url="/auth/login",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    app = Application()
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
