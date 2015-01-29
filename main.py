from flask import Flask, render_template, url_for
app = Flask(__name__)
app.config['DEBUG'] = True

import urllib
#from google.appengine.api import users
#from google.appengine.ext import ndb

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')




@app.errorhandler(404)
def page_not_found(e):
    """return a custom 404 error."""
    return 'sorry, nothing at this url.', 404



if __name__ == '__main__':
    app.run(debug=True)
