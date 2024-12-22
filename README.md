<!-- You should add a readme correct any of this if its wrong--> 
<!-- You should restructure the files to have a backend and frontend folder -->

# WordHuntFinder
A simple word hunt finder that finds words in a grid of letters.
Implemented in Python using a Trie data structure, and a Breadth First Search algorithm. 
A basic frontend was also developed using React and Typescript.

## How to run
1. Clone the repository
2. Run the backend
    - Navigate to the `backend` directory
    - Create a virtual environment (optional)
    - Run `pip install -r requirements.txt`
    - Cd into the `app` directory
    - Run `python app.py`
3. Run the frontend
    - Navigate to the `frontend` directory
    - Run `npm install`
    - Run `npm run dev`
    - Open `http://localhost:5173` in your browser


## How it works
The frontend user interface allows the user to input a grid of letters they wish to find all the possible words in following the rules of the game word hunt.
The frontend sends the grid of letters to the backend which then finds all the possible words in the grid and returns them to the frontend.
The frontend then displays the words found in the grid to the user.

