from flask import Flask
from flask import render_template, url_for
from flask import request
from flask import jsonify
from flask import make_response

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True      
app.jinja_env.auto_reload = True
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/", methods = ['GET', 'POST'])
def htmlRequest():
    viewModel = {
        "headers": request.headers,
        "querystring": request.args,
        "payload": request.form,
        "json": request.json
    }

    return render_template('index.html', viewModel = viewModel)

@app.route("/post", methods = ['GET'])
def postFormRequest():
    return render_template('form.html')    

# request.data 
# request.args: query string
# request.form: HTML form
# request.files: HTML form files
# request.values: args and form, args first
# request.json: application/json content-type

@app.route("/json", methods = ['GET', 'POST'])
def jsonRequest():
    viewModel = {
         "headers": { k:v for k, v in request.headers.items()},
         "querystring": { k:v for k, v in request.args.items()},
         "payload": { k:v for k, v in request.form.items()},
         "json": { k:v for k, v in request.json.items()}
    }
    print({ k:v for k, v in request.form.items()})
    return jsonify(viewModel)

@app.errorhandler(404)
def page_not_found(error):
    return make_response(render_template('404.html', error=error), 404)