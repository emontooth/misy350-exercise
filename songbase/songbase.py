from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
 #    return "hello people"
 return render_template('index.html')


@app.route('/form', method=['GET', 'POST'])
def form():
    if request.method == "GET":
        return render_template('form.html')
    if request.method == "POST":
        #return "Got your data!!! This is how you post a message to the page after hitting submit."
        first_name = request.form["first_name"]
        #return "hi, your name is %s" % first_name
        return render_template('form.html', first_name=first_name)
        


@app.route('/users/<string:username>')
def users(username):

    #    return "hello %s", username
    return render_template('user.html', username=username)


@app.route('/user')
def user():
        return "this is a user page"




if __name__ == '__main__':
        app.run()

        app.run(debug=True)

        app.run(host='0.0.0.0', port=4500)
