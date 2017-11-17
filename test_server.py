from flask import Flask
from flask import request

app=Flask(__name__)

# router rules
@app.route('/')
def index():
  return "Index Page"

@app.route('/my')
def my_page():
  return "my page"

#route var rules
# string 
@app.route('/user/<username>')
def user_info(username):
  return 'user is %s' % username

# int,float,path
@app.route('/post/<int:post_id>')
def client_post(post_id):
  return 'recieve client id %s' % post_id

"""构造 URL url_for(func,param)
"""

@app.route('/login')
# def login():pass

@app.route('/user/<username>')
def profile(username):pass

with app.test_request_context():
  print url_for('index') #/
  print url_for('login') #/login
  print url_for('login', next='/') #/login?next=/
  print url_for('profile',username='John Doe') #/usr/Jhon%20Doe

"""HTTP方法支持
"""

@app.route('login',method=['GET','POST'])
def login():
  if request.method=='POST':
    print('Client Post')
  else:
    print('Client Get')








if __name__=='__main__':
  # app.run()
  # debug mode
  app.run(debug=True)

