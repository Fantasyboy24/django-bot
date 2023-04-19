from flask import Flask, request, jsonify, render_template
from gpt_index import GPTSimpleVectorIndex
import os

app = Flask(__name__)
os.environ['OPENAI_API_KEY'] = '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'
index = GPTSimpleVectorIndex.load_from_disk('index.json')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask_bot', methods=['POST'])
def ask_bot():
    query = request.form['input']  # get user's query from the form
    response = index.query(query, response_mode='compact')  # call the ask_bot function
    return jsonify({'response': response.response})

if __name__ == '__main__':
    app.run(debug=True)
