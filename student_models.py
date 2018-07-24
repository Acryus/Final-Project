from google.appengine.ext import ndb

class Student(ndb.Model):
    firstName = ndb.StringProperty(required=True)
    lastName = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    college = ndb.StringProperty(required=True)
    major = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
    connections = ndb.StringProperty(repeated=True,required=False)

class areasOfInterest(ndb.Model):
    interests = ndb.KeyProperty(Student, repeated=True, required = False)

class areasOfHelp(ndb.Model):
    help = ndb.KeyProperty(Student, repeated=True, required = False)
