from flask import Flask, jsonify, request, render_template, session
from flask_cors import CORS

import sys
import os

# I think because I'm on mac I had to adjust the path joiner by ../ so change back for you
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from Solver.solver import Solver
from Trie.trie import Trie

app = Flask(__name__.split('.')[0])
CORS(app)

with open('../../trie_data.pickle', 'r') as file:
    valid_words = Trie()
    valid_words.deserialize_from_file('../../trie_data.pickle', format='pickle')

@app.route("/")
def home():
    return render_template("index.html")

@app.post("/wordhunt")
def wordhunt_post():
    data = request.get_json()
    letters = data['letters']

    if not letters:
        return f"No letters provided", 400
    
    solver = Solver(letters, 'wordhunt')
    found_words = solver.solve_word_hunt(valid_words)
    return sorted(list(found_words), key=lambda x: len(x), reverse=True)

@app.post("/anagrams")
def anagrams_post():
    data = request.get_json()
    letters = data['letters']

    if not letters:
        return f"No letters provided", 400

    solver = Solver(letters, 'anagrams')
    found_words = solver.solve_anagrams(valid_words)
    return sorted(list(found_words), key=lambda x: len(x), reverse=True)

if __name__ == '__main__':
    app.run(debug=True)
