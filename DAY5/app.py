# Create the app
from flask import Flask, render_template

# Create Flask app
app = Flask(__name__)

# List of UI/UX topics from your BCA syllabus
topics = [
    {"id": 1, "name": "Fundamentals of UX and UI", "description": "Basic concepts of User Experience and User Interface design", "hours": 4},
    {"id": 2, "name": "UX vs UI", "description": "Differences between UX and UI designers and their roles", "hours": 2},
    {"id": 3, "name": "UX Principles", "description": "Usability, Accessibility, Simplicity", "hours": 3},
    {"id": 4, "name": "Core UX Disciplines", "description": "User research, IA, Interaction design, Visual design", "hours": 5},
    {"id": 5, "name": "User Interfaces Types", "description": "CLI, GUI, VUI, Menu-driven, NLP-based", "hours": 3},
]

@app.route('/topics')
def topics_list():
    """Show all UI/UX topics"""
    # Pass the entire topics list to the template
    return render_template('topics.html', title="Topics - UI/UX Syllabus", topics=topics)

@app.route('/student')
def student_form():
    return render_template('student_form.html', title='Student Form')

# 3. Homepage route
@app.route('/')
def home():
    # This runs when someone visits /
    return '''
    <h1>📘 BCA UI/UX Notes</h1>
    <p>Welcome to your study notebook server.</p>
    <p>Try these links:</p>
    <ul>
        <li><a href="/about">About this project</a></li>
        <li><a href="/user/student">Dynamic user page</a></li>
    </ul>
    '''

# 4. About page
@app.route('/about')
def about():
    return '''
    <h1>About This Flask App</h1>
    <p>This app is part of your BCA UI/UX notebook.</p>
    <p>Flask helps you turn Python code into web pages.</p>
    <a href="/">← Back to Home</a>
    '''

# 5. Dynamic user page
@app.route('/user/<username>')
def user_profile(username):
    # Show different content based on the URL
    return f'''
    <h1>👤 User Profile: {username}</h1>
    <p>This page is personalized for {username}.</p>
    <p>In a real app, you would load data from a database here.</p>
    <a href="/">← Back to Home</a>
    '''

# 6. Run the server
if __name__ == '__main__':
    # debug=True means: 
    # - Server restarts when you save code
    # - Shows error messages in browser (helpful for learning)
    app.run(debug=True)