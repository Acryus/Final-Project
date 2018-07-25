from google.appengine.ext import ndb

class Student(ndb.Model):
    firstName = ndb.StringProperty(required=True)
    lastName = ndb.StringProperty(required=True)
    state = ndb.StringProperty(required=True)
    college = ndb.StringProperty(required=True)
    major = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
    interests = ndb.StringProperty(repeated=True)
    help = ndb.StringProperty(repeated=True)
