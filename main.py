import webapp2
import os
import jinja2
from student_models import Student, areasOfHelp, areasOfInterest

jina_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        home_template = jinja_env.get_template("templates/homepage.html")
class ListHandler(webapp2.RequestHandler):
    def get(self):
        list_template = jinja_env.get_template()#input Ritu's template with quotations)
        self.response.write(start_template.render())

class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        pass
class SignUpHandler(webapp2.RequestHandler):
    def get(self):
        signUpTemplate = jinja_env.get_template("templates/createProfile.html")
        html = main_template.render()
        newStudent = model.Student()


        self.response.write(html)

class SignInHandler(webapp2.RequestHandler):
    def get(self):
        signUpTemplate = jinja_env.get_template("")
        html = main_template.render()
        self.response.write(html)

class SearchHandler(webapp2.RequestHandler):
    def get(self):
        signUpTemplate = jinja_env.get_template("")
        html = main_template.render()
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/list', ListHandler),
    ('/profile/' , #nameofStudent
    ProfileHandler),
    ("/search", SearchHandler),
    ('/signup', SignUpHandler),
    ('/signin', SignInHandler)
], debug=True)
