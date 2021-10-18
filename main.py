from pathlib import Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

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
    if request.method == "POST":
        if request.form:
            bitNumber = request.form.get("bits")
            if len(bitNumber) != 0:
                return render_template("layouts/binary.html", BITS=int(bitNumber), imageOn="/static/assets/exciteddog.jpeg", imageOff="/static/assets/sleepingdog.jpeg")
        if request.form["bits2"]:
            return render_template("layouts/binary.html", BITS=8, imageOn="/static/assets/exciteddog.jpeg", imageOff="/static/assets/sleepingdog.jpeg")
    return render_template("layouts/binary.html", BITS=8, imageOn="/static/assets/exciteddog.jpeg", imageOff="/static/assets/sleepingdog.jpeg")

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

@app.route('/BinaryRGB/', methods=['GET', 'POST'])
def BinaryRGB():
    return render_template("layouts/binaryrgb.html")

@app.route('/binaryrgb/', methods=['GET', 'POST'])
def binaryrgb():
    return render_template("layouts/binaryrgb.html")

@app.route('/signedaddition/', methods=['GET', 'POST'])
def signedaddition():
    return render_template("layouts/signedaddition.html")

@app.route('/unicode/', methods=['GET', 'POST'])
def unicodee():
    return render_template("layouts/unicode.html")

@app.route('/unsignedaddition/', methods=['GET', 'POST'])
def unsignedaddition():
    return render_template("layouts/unsignedaddition.html")

@app.route('/logicgates/', methods=['GET', 'POST'])
def logicgates():
    return render_template("layouts/logicgates.html")

@app.route('/favorbooks/', methods=['GET', 'POST'])
def favorbooks():
    return render_template("layouts/favorbooks.html")

@app.route('/stanley/', methods=['GET', 'POST'])
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

@app.route('/listdictionary/', methods=['GET', 'POST'])
def listdictionary():
    return render_template("layouts/unicode.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)