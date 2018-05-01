from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
 #    return "hello people"
 return render_template


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
