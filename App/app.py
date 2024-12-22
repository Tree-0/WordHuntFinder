from flask import Flask, jsonify, request, render_template, session
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Solver.solver import Solver
from Trie.trie import Trie

app = Flask(__name__.split('.')[0])

# get the trie of all valid words from file
with open('trie_data.pickle', 'r') as file:
    valid_words = Trie()
    valid_words.deserialize_from_file('trie_data.pickle', format='pickle')

# home page 
@app.route("/")
def home():
    return render_template("index.html")

# send letters to solve wordhunt
@app.post("/wordhunt")
def wordhunt_post():
    letters = request.form.get('letters')
    if not letters:
        return f"No letters provided", 400
    
    # solve the wordhunt
    solver = Solver(letters, 'wordhunt')
    found_words = solver.solve_word_hunt(valid_words)
    return sorted(list(found_words), key=lambda x: len(x), reverse=True)

# send letters to solve anagrams
@app.post("/anagrams")
def anagrams_post():
    letters = request.form.get('letters')
    if not letters:
        return f"No letters provided", 400

    # solve the anagrams
    solver = Solver(letters, 'anagrams')
    found_words = solver.solve_anagrams(valid_words)
    return sorted(list(found_words), key=lambda x: len(x), reverse=True)

if __name__ == '__main__':
    app.run(debug=True)