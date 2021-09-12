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
    return render_template("layouts/binary.html")

# connects /kangaroos path to render nighthawkreviews.html

@app.route('/tianbin/', methods=['GET', 'POST'])
def tianbin():
    # submit button has been pushed
    print("1")
    if request.form:
        print("2")
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            print("3")
            return render_template("layouts/tianbin.html", name1=name)
    # starting and empty input default
    return render_template("layouts/tianbin.html", name1="World")

@app.route('/justin/', methods=['GET', 'POST'])
def justin():
    # submit button has been pushed
    print("1")
    if request.form:
        print("2")
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            print("3")
            return render_template("layouts/justin.html", name1=name)
    # starting and empty input default
    return render_template("layouts/justin.html", name1="World")

@app.route('/concepts/', methods=['GET', 'POST'])
def concepts():
    # submit button has been pushed
    print("1")
    if request.form:
        print("2")
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            print("3")
            return render_template("layouts/concepts.html", name1=name)
    # starting and empty input default
    return render_template("layouts/concepts.html", name1="World")

@app.route('/aboutus/', methods=['GET', 'POST'])
def aboutus():
    # submit button has been pushed
    print("1")
    if request.form:
        print("2")
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            print("3")
            return render_template("layouts/aboutus.html", name1=name)
    # starting and empty input default
    return render_template("layouts/aboutus.html", name1="World")

@app.route('/popularnow/', methods=['GET', 'POST'])
def popularnow():
    return render_template("layouts/popularnow.html")

@app.route('/nighthawkreviews/', methods=['GET', 'POST'])
def nighthawkreviews():
    return render_template("layouts/nighthawkreviews.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
