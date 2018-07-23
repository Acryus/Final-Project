from google.appengine.ext import ndb

class Student(ndb.Model):
    firstName =  ndb.StringProperty(required=True)
    lastName =  ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    college = ndb.StringProperty(required=True)
    zipCode = ndb.StringProperty(required=True)
    areasOfInterests = ndb.StringProperty(required=True)
    areasOfHelp = ndb.StringProperty(required=True)

class House(ndb.Model):
      name = ndb.StringProperty(required=True)
      mascot = ndb.StringProperty(required=False)
      students = ndb.KeyProperty(Student, repeated=True)
