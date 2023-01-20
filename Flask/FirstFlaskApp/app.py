from flask import Flask, request, render_template, redirect
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chickens'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

MOVIES = ['Jurrasic Park', 'Pulp Fiction', 'Step Brothers']

@app.route('/')
def home_page():
    html = '''
    <html>
        <body>
            <h1>Home Page</h1>
            <p>Welcome to my first app</p>
            <a href='/hello'>Go to hello page</a>
            <a href='/goodbye'>Go to goodbye page</a>
        </body>
    </html>
    '''
    return render_template('home.html')

@app.route('/old-home-page')
def redirect_to_home():
    return redirect('/')

@app.route('/hello')
def say_hello():
    return render_template('hello.html')

@app.route('/goodbye')
def say_goodbye():
    return render_template('goodbye.html')

@app.route('/lucky')
def lucky_number():
    num = randint(1, 10)
    msg = 'You are so lucky'
    return render_template('lucky.html', lucky_num=num, msg=msg)

@app.route('/form')
def show_form():
    return render_template('form.html')

@app.route('/form-2')
def show_form_2():
    return render_template('form_2.html')

@app.route('/spell/<word>')
def spell_word(word):
    caps_word = word.upper()
    return render_template('spell_word.html', word=caps_word)

COMPLIMENTS = ['cool', 'clever', 'good looking', 'awesome', 'pythonic']

@app.route('/greet')
def get_greeting():
    username = request.args.get('username')
    nice_thing = choice(COMPLIMENTS)
    return render_template('greet.html', username=username, compliment=nice_thing)

@app.route('/greet-2')
def get_greeting_2():
    username = request.args.get('username')
    wants = request.args.get('wants_compliments')
    nice_things = sample(COMPLIMENTS,3)
    return render_template('greet_2.html', username=username, wants_compliments=wants, compliments=nice_things)

@app.route('/search')
def search():
    term = request.args['term']
    sort = request.args['sort']
    return f'<h1>Search Results for: {term}</h1><p>Sorted by {sort}</p>'

# @app.route('/post', methods=['POST'])
# def post_demo():
#     return 'You made a POST request'

# @app.route('/post', methods=['Get'])
# def get_demo():
#     return 'You made a GET request'

@app.route('/add-comment')
def add_comment_form():
    return '''
    <h1>Add Comment</h1>
    <form method='POST'>
        <input type='text' placeholder='comment' name='comment'/>
        <input type='text' placeholder='username' name='username'/>
        <button>Submit</button>
    </form>
    '''

@app.route('/add-comment', methods=['POST'])
def save_comment():
    comment = request.form['comment']
    username = request.form['username']
    print(request.form)
    return f'''
    <h1>Saved Your Comment</h1>
    <h2>{comment}</h2>
    <h3>Posted by {username}</h3>
    '''

@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f'''
    <h1>reddit/r/{subreddit}</h1>
    <p>Welcome to the {subreddit} subreddit</p>
    '''

@app.route('/r/<subreddit>/comments/<int:post_id>')
def show_comments(subreddit, post_id):
    return f'''
    <h1>reddit/r/{subreddit}</h1>
    <p>Post id:{post_id} in the {subreddit} subreddit</p>
    '''   
    

POSTS = {
    1: 'I love chicken',
    2: 'I hate chicken',
    3: 'I have no strong opinions about chicken',
    4: 'A chicken killed my family'
}

@app.route('/posts/<int:id>')
def find_post(id):
    post = POSTS.get(id, 'Post not found')
    return f'''
    <h1>Posts</h1>
    <p>{post}</p>
    '''

