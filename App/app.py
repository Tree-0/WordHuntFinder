from flask import Flask, jsonify, request, render_template, session
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Solver.solver import Solver
from Trie.trie import Trie

app = Flask(__name__.split('.')[0])

with open('trie_data.pickle', 'r') as file:
    valid_words = Trie()
    valid_words.deserialize_from_file('trie_data.pickle', format='pickle')

@app.route("/")
def home():
    return render_template("index.html")

@app.post("/wordhunt")
def wordhunt_post():
    letters = request.form.get('letters')
    if not letters:
        return f"No letters provided", 400
    
    solver = Solver(letters, 'wordhunt', 4)
    found_words = solver.solve_word_hunt(valid_words)
    return list(found_words)

@app.post("/anagrams")
def anagrams_post():
    letters = request.form.get('letters')
    if not letters:
        return f"No letters provided", 400

    solver = Solver(letters, 'anagrams', 7)
    found_words = solver.solve_anagrams(valid_words)
    return list(found_words)

if __name__ == '__main__':
    app.run(debug=True)