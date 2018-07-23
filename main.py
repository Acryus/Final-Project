import webapp2
import os
import jinja2
from student_models import Student

jina_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Welcome to Hogwarts' Online Portal")

class HouseHandler(webapp2.RequestHandler):
    def get(self):
        hogwarts_houses = House.query().order(House.name).fetch()
        start_template = jinja_env.get_template("templates/houselist.html")
        self.response.write(start_template.render({'house_info' : hogwarts_houses}))

class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/houses', HouseHandler),
    ('/seed-data', LoadDataHandler)
], debug=True)
