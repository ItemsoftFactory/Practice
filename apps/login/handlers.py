__author__ = 'ai00135'
from views import *

app = webapp2.WSGIApplication([
    ('/', Sign_up)
], debug=True)
