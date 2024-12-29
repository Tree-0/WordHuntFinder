import { Dispatch, SetStateAction } from "react";
import { fetchWordHuntSolutions } from "./data";

// Convert 2D array to a single string
export const generateBoardString = (board: string[][]): string => {
  return board.flat().join('');
}

// Fill the board with empty strings
export const handleClearBoard = (setBoard: Dispatch<SetStateAction<string[][]>>, gridSize: number) => {
  setBoard(Array(gridSize).fill("").map(() => Array(gridSize).fill("")));
}

// If grid is getting larger, we need to add new rows and columns filled with blanks
// If grid is getting smaller, we need to remove rows and columns from rightmost columns and bottommost rows
export const handleGridSizeChange = (setBoard: Dispatch<SetStateAction<string[][]>>, setGridSize: Dispatch<SetStateAction<number>>, board: string[][], size: number) => {
  setGridSize(size);

  // Do the 360 no scope
  const newBoard = Array(size)
    .fill("")
    .map((_, i) =>
      Array(size)
        .fill("")
        .map((_, j) => (board[i]?.[j] ?? ""))
    );

  setBoard(newBoard);
}

// Generate a 2D array filled with empty strings -- Initialization phase
export const generateBoard = (size: number): string[][] => {
  return Array(size)
    .fill("")
    .map(() => Array(size).fill(""));
}

// Update the board with the new value
export const handleInputChange = (row: number, col: number, value: string, board: string[][], setBoard: Dispatch<SetStateAction<string[][]>>) => {
  // Ensure only one character is entered even though we want the event to be triggered on every key press
  if (value.length > 1) {
    value = value[value.length - 1]; // Ensure only the last character is considered
  }

  if (!/^[a-zA-Z]?$/.test(value)) return; // Allow only letters

  // Update the board
  const newBoard = board.map((r, i) =>
    r.map((cell, j) => (i === row && j === col ? value.toUpperCase() : cell))
  );
  setBoard(newBoard);
}

// Call the API to fetch solutions
export const handleSubmit = async (event: React.FormEvent, gridSize: number, board: string[][], setResults: Dispatch<SetStateAction<string[]>>, setError: Dispatch<SetStateAction<string>>, setCurrentItem: Dispatch<SetStateAction<number>>) => {
  event.preventDefault();
  const letters = generateBoardString(board);

  if (letters.length !== gridSize * gridSize) {
    setError('Please fill all cells in the grid.');
    return;
  }

  setError('');
  setResults([]);

  // Fetch solutions
  const solutions = await fetchWordHuntSolutions(letters);

  if (solutions.length === 0) {
    setError('No words found.');
    return;
  } else if (solutions.length === 1 && solutions[0].startsWith('Error:')) {
    setError(solutions[0]);
    return;
  } else {
    setResults(solutions);
    setCurrentItem(0);
  }
}
