from flask import Flask, redirect, url_for, render_template, request, flash
 
app = Flask(__name__,template_folder='templates')
 
app.debug = True


@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return f'welcome to a POST of {user}'
   else:
      return 'welcome to a GET'
 
@app.route('/users/<user_id>', methods = ['GET', 'POST', 'DELETE'])
def user(user_id):
    if request.method == 'GET':
        return 'You are running GET method for '+ user_id + ' user'
    if request.method == 'POST':
        return 'You are running POST method for '+ user_id + ' user ' 
    if request.method == 'DELETE':
        return 'You are running DELETE method for '+ user_id + ' user '



app.run(host='0.0.0.0', port=99)



# donde ver las paginas
#>http://localhost:99/form
#>http://localhost:99/login
#>http://localhost:99/users/Nuria#