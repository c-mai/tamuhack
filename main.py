# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
# [START gae_python3_app]
from flask import Flask, render_template, request, redirect, url_for
from disaster import disaster_api_call

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def index():
    """Return a friendly HTTP greeting."""
    return render_template("index.html")

@app.route('/success/<location>')
def success(location):
   return render_template("success.html", loc = location, data = str(disaster_api_call(location)))
  
@app.route('/location',methods = ['POST', 'GET'])
def location_submission():
   if request.method == 'POST':
      loc = request.form['nm']
      return redirect(url_for('success',location = loc))
   else:
      loc = request.args.get('nm')
      return redirect(url_for('success',location = loc))

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
