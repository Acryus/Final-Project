import webapp2
import os
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb

jina_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class WelcomeHandler(webapp2.RequestHandler):
      def get(self):
        user = users.get_current_user()
        # If the user is logged in...
        if user:
          email_address = user.nickname()
          cssi_user = CssiUser.get_by_id(user.user_id())
          signout_link_html = '<a href="%s">sign out</a>' % (
              users.create_logout_url('/HomeHandler'))
          # If the user has previously been to our site, we greet them!
          if cssi_user:
            self.response.write('''
                Welcome %s %s (%s)! <br> %s <br>''' % (
                  cssi_user.first_name,
                  cssi_user.last_name,
                  email_address,
                  signout_link_html))
          # If the user hasn't been to our site, we ask them to sign up
          else:
              template = jinja_env.get_template("templates/createProfile.html")
              self.response.write(template.render({
              'first_name' : firstName,
              "last_name" : lastName,
              "college": college,
              "state": state,
              "major": major,
              "description": description,
              "interests": interests,
              "help": help
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
        cssi_user = CssiUser(
            first_name=self.request.get('first_name'),
            last_name=self.request.get('last_name'),
            id=user.user_id())
        cssi_user.put()
        self.response.write('Thanks for signing up, %s!' %
            cssi_user.first_name)

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

class SearchHandler(webapp2.RequestHandler):
    def get(self):
        signUpTemplate = jinja_env.get_template("")
        html = signUpTemplate.render()
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
    ('/home', HomeHandler)
    ('/list', ListHandler),
    ('/profile/' # + nameOfStudent
    ,ProfileHandler)
    ("/search", SearchHandler)
], debug=True)
