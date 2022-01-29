
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def main():
   return render_template('index.html')
  
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name
  
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      location = request.form['nm']
      return redirect(url_for('success',name = location))
   else:
      location = request.args.get('nm')
      return redirect(url_for('success',name = location))
  
if __name__ == '__main__':
   app.run(debug = True)