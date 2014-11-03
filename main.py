import webapp2
import os
from models import File
#from views import MainPage, About, New

# from flask import Flask
# app = Flask(__name__)
# app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')




app = webapp2.WSGIApplication([('/', MainPage), ], debug=True)