# Flask-Reflection

[Python Flask Header & Payload Reflection](https://sdwh.dev/posts/2022/11/Python-Flask-Header-Payload-Reflection/)

### 安裝 Flask

```batch
mkdir flask
cd flask
python3 -m venv venv
venv\Scripts\activate
pip install Flask
```

啟動 flask

```batch
flask --app main run
flask --app main --debug run
```

### Flask 結構

/main.py
/templates/base.html
/templates/index.html
/templates/form.html
/templates/404.html

### 後端框架實現功能

**Routing**

```python
@app.route("/", methods = ['GET', 'POST'])
def htmlRequest():
    if request.method == 'GET':
      ...
    if request.method =='POST':
      ...
```

**Error Handle**

```python
@app.errorhandler(404)
def page_not_found(error):
    return make_response(render_template('404.html', error=error), 404)
```

**Json Response**

```python
from flask import jsonify

@app.route("/json", methods = ['GET', 'POST'])
def jsonRequest():
    viewModel = {
         "headers": { k:v for k, v in request.headers.items()},
    }
    return jsonify(viewModel)
```

**Url Generate**

```html
<a class="btn btn-primary" href="{{ url_for('postFormRequest') }}">Post Form</a>

<form method="post" action="{{ url_for('htmlRequest', foo=10, bar=30) }}">
  ...
</form>
```

**HTTP Data Handle**

注意 request 的資料物件不是 Dict 在 <kbd>jsonift</kbd> 會發生例外錯誤，必須主動透過 <kbd>dict generator</kbd> 轉換為 dict 以正確處理。

```python
viewModel = {
      "headers": { k:v for k, v in request.headers.items()},
      "querystring": { k:v for k, v in request.args.items()},
      "payload": { k:v for k, v in request.form.items()},
      "json": { k:v for k, v in request.json.items()}
}
```
