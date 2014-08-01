__author__ = 'ai00135'

from settings import *
from models import *
class Sign_up(Handler):
    def get(self):
        users = ndb.gql('SELECT * FROM CustomerUser')
        self.render("index.html", users=users)

    def post(self):
        user = CustomerUser(name=self.request.get('nombre'),
                    email=self.request.get('email'),
                    age=int(self.request.get('edad')),
                    city=self.request.get('ciudad'))
        user.put()
        self.redirect("/")
