from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Mock AI responses (simulating Bedrock/GCP)
code_explanations = {
    "loop": "This is a for loop that iterates through items",
    "array": "Arrays store multiple values in a single variable",
    "function": "Functions are reusable blocks of code"
}

practice_problems = {
    "arrays": ["LeetCode #1 Two Sum", "LeetCode #217 Contains Duplicate"],
    "loops": ["HackerRank Loop Practice", "LeetCode #495 Teemo Attacking"],
    "functions": ["HackerRank Function Challenge", "CodeStudio Recursion"]
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/api/explain', methods=['POST'])
def explain_code():
    data = request.json
    code = data.get('code', '')
    language = data.get('language', 'English')

    # Mock explanation
    explanation = f"Explanation of your code in {language}: This code demonstrates good practices."
    return jsonify({'explanation': explanation, 'language': language})


@app.route('/api/practice', methods=['POST'])
def get_practice():
    data = request.json
    topic = data.get('topic', 'arrays')

    return jsonify({
        'problems': practice_problems.get(topic, []),
        'topic': topic
    })


@app.route('/api/future-courses', methods=['GET'])
def future_courses():
    return jsonify({
        'arrays': ['Data Structures', 'Algorithms'],
        'loops': ['Advanced Programming', 'Competitive Coding'],
        'functions': ['Recursion', 'Functional Programming']
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
