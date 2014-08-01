__author__ = 'ai00135'
import sys
from google.appengine.ext import ndb
sys.modules['ndb'] = ndb
import webapp2_extras.appengine.auth.models as auth_models

class CustomerUser(ndb.Model):
    name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    age = ndb.IntegerProperty(required=True)
    city = ndb.StringProperty(required=True)