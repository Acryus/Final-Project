import webapp2
import os
import jinja2
from student_models import Student
from google.appengine.api import users
from google.appengine.ext import ndb

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class WelcomeHandler(webapp2.RequestHandler):
      def get(self):
        user = users.get_current_user()
        # If the user is logged in...
        if user:
          email_address = user.nickname()
          cssi_user = Student.get_by_id(user.user_id())
          signout_link_html = '<a href="%s">sign out</a>' % (
              users.create_logout_url('/HomeHandler'))
          # If the user has previously been to our site, we greet them!
          if cssi_user:
            self.response.write('''
                Welcome %s %s (%s)! <br> %s <br>''' % (
                  cssi_user.firstName,
                  cssi_user.lastName,
                  email_address,
                  signout_link_html))
          # If the user hasn't been to our site, we ask them to sign up
          else:
              template = jinja_env.get_template("templates/createProfile.html")
              self.response.write(template.render({
              'first_name' : Student.firstName,
              "last_name" : Student.lastName,
              "college": Student.college,
              "state": Student.state,
              "major": Student.major,
              "description": Student.description#,
              ##"interests": interests,
              ##"help": help
              }))

        # Otherwise, the user isn't logged in!
        else:
          self.response.write('''
            Please log in to use our site! <br>
            <a href="%s">Sign in</a>''' % (
              users.create_login_url('/')))

      def post(self):
        user = users.get_current_user()
        if not user:
          # You shouldn't be able to get here without being logged in
          self.error(500)
          return
        cssi_user = Student(
            firstName=self.request.get('first_name'),
            lastName=self.request.get('last_name'),
            college=self.request.get('college'),
            state=self.request.get('state'),
            major=self.request.get('major'),
            description=self.request.get('descriptions'),
            id=user.user_id())
        cssi_user.put()
        self.response.write('Thanks for signing up, %s!' %
            cssi_user.firstName)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        home_template = jinja_env.get_template("templates/homepage.html")
        self.response.write(home_template.render())

class ListHandler(webapp2.RequestHandler):
    def get(self):
        list_template = jinja_env.get_template("templates/listpage.html")
        self.response.write(list_template.render())

class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        pass
class SearchHandler(webapp2.RequestHandler):
    def get(self):
        signUpTemplate = jinja_env.get_template("")
        html = signUpTemplate.render()
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
    ('/home', HomeHandler),
    ('/list', ListHandler),
    ('/profile/' # + nameOfStudent
    ,ProfileHandler),
    ("/search", SearchHandler),
], debug=True)
