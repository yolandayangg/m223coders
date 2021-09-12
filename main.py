# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

# connects default URL to render index.html
@app.route('/binary/')
def binary():
    return render_template("binary.html")

# connects /kangaroos path to render stanley.html

@app.route('/yolanda/', methods=['GET', 'POST'])
def yolanda():
    # submit button has been pushed
    print("1")
    if request.form:
        print("2")
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            print("3")
            return render_template("yolanda.html", name1=name)
    # starting and empty input default
    return render_template("yolanda.html", name1="World")

@app.route('/stanley/', methods=['GET', 'POST'])
def stanley():
    # submit button has been pushed
    print("1")
    if request.form:
        print("2")
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            print("3")
            return render_template("stanley.html", name1=name)
    # starting and empty input default
    return render_template("stanley.html", name1="World")

@app.route('/tianbin/', methods=['GET', 'POST'])
def tianbin():
    # submit button has been pushed
    print("1")
    if request.form:
        print("2")
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            print("3")
            return render_template("tianbin.html", name1=name)
    # starting and empty input default
    return render_template("tianbin.html", name1="World")

@app.route('/justin/', methods=['GET', 'POST'])
def justin():
    # submit button has been pushed
    print("1")
    if request.form:
        print("2")
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            print("3")
            return render_template("justin.html", name1=name)
    # starting and empty input default
    return render_template("justin.html", name1="World")

@app.route('/minilab/', methods=['GET', 'POST'])
def minilab():
    # submit button has been pushed
    print("1")
    if request.form:
        print("2")
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            print("3")
            return render_template("minilab.html", name1=name)
    # starting and empty input default
    return render_template("minilab.html", name1="World")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
