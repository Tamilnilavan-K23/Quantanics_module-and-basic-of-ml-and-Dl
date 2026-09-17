from flask import Flask

app=Flask(__name__)

@app.route('/hello')
def hello():
       return '<p>Hello!</p>'

@app.route('/')
def hello_world():
    return '<p>Hello, World!<p>'

#variable route
@app.route ('/user/<username>')
def show(username):
     return  f'The User is {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    
    return f'Post {post_id}'

if __name__ == '__main__':
    app.run()
 