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

# connects /kangaroos path to render reviews.html

@app.route('/yolanda/', methods=['GET', 'POST'])
def yolanda():
    # submit button has been pushed
    print("1")
    if request.form:
        print("2")
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            print("3")
            return render_template("layouts/yolanda.html", name1=name)
    # starting and empty input default
    return render_template("layouts/yolanda.html", name1="World")

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

@app.route('/reviews/', methods=['GET', 'POST'])
def reviews():
    return render_template("layouts/reviews.html")

@app.route('/questions/', methods=['GET', 'POST'])
def questions():
    return render_template("layouts/questions.html")

@app.route('/discussion/', methods=['GET', 'POST'])
def discussion():
    return render_template("layouts/discussion.html")

@app.route('/rgb/', methods=['GET', 'POST'])
def rgb():
    return render_template("layouts/rgb.html")

@app.route('/stanley', methods=['GET', 'POST'])
def stanley():
    # submit button has been pushed
    print("1")
    if request.form:
        print("2")
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            print("3")
            return render_template("layouts/stanley.html", name1=name)
    # starting and empty input default
    return render_template("layouts/stanley.html", name1="World")

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

@app.route('/justin', methods=['GET', 'POST'])
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


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)