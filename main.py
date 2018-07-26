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

          # If the user has previously been to our site, we greet them!
          if cssi_user:
            return webapp2.redirect("/home")
          # If the user hasn't been to our site, we ask them to sign up
          else:
              template = jinja_env.get_template("templates/createProfile.html")
              self.response.write(template.render())
        # Otherwise, the user isn't logged in!
        else:
          self.response.write('''
            Please log in to use our site! <br>
            <a href="%s">Sign in</a>''' % (
              users.create_login_url('/signup')))

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
            description=self.request.get('desc'),
            id=user.user_id())
        cssi_user.put()
        self.redirect("/home")

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        home_template = jinja_env.get_template("templates/homepage.html")
        self.response.write(home_template.render( {"loginUrl" : users.create_login_url('/signup')}))

class HomeHandler2(webapp2.RequestHandler):
    def get(self):
        home2_template = jinja_env.get_template("templates/homepage2.html")
        self.response.write(home2_template.render())

class SearchHandler(webapp2.RequestHandler):
    def get(self):
        searchTemplate = jinja_env.get_template("templates/search.html")
        if self.request.get("state") == "":
            students = Student.query().fetch()
        else
            students = Student.query().filter(Student.state == self.request.get("state")).fetch()

        html = searchTemplate.render(
        {
            "students": students
        }
        )
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/signup', WelcomeHandler),
    ('/', HomeHandler),
    ('/home', HomeHandler2),
    ("/search", SearchHandler),
], debug=True)
