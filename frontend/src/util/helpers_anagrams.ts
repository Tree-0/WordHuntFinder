import { Dispatch, SetStateAction } from "react";
import {fetchAnagramsSolutions} from "./data";

// Generate Board String?
export const generateBoardString = (board: string[]): string => {
    return board.join('');
}

// Fill the board with empty strings
export const handleClearBoard = (setBoard: Dispatch<SetStateAction<string[]>>, stringSize: number) => {
    setBoard(Array(stringSize).fill(""));
}

// When grid changes, preserve letters
export const handleGridSizeChange = (setBoard: Dispatch<SetStateAction<string[]>>, setStringSize: Dispatch<SetStateAction<number>>, board: string[], size: number) => {
    setStringSize(size);

    const newBoard = Array(size)
    .fill("")
    .map((_, i) => (board[i] ?? ""))

    setBoard(newBoard);
}

// init an array of of empty strings -- Initialization phase
export const generateBoard = (size: number): string[] => {
    return Array(size).fill("");
}

// Update board with new value
export const handleInputChange = (col: number, value: string, board: string[], setBoard: Dispatch<SetStateAction<string[]>>) => {
    // Each cell should only hold one letter
    if (value.length > 1) {
        value = value[value.length - 1]; // Ensure only the last character is considered
    }

    if (!/^[a-zA-Z]?$/.test(value)) return; // Allow only letters

    // update board
    const newBoard = board.map((v,i) => (i === col ? value.toUpperCase() : v));

    setBoard(newBoard);
}

// Call API to get anagrams solutions
export const handleSubmit = async (event: React.FormEvent, stringSize: number, board: string[], setResults: Dispatch<SetStateAction<string[]>>, setError: Dispatch<SetStateAction<string>>, setCurrentItem: Dispatch<SetStateAction<number>>) => {
    event.preventDefault();
    const letters = generateBoardString(board);

    if (letters.length !== stringSize) {
        setError('Please fill all cells in the board');
        return;
    }

    setError('');
    setResults([]);

    const solutions = await fetchAnagramsSolutions(letters);

    if (solutions.length === 0) {
        setError('No words found.');
        return;
    } else if (solutions.length === 1 && solutions[0].startsWith('Error:')) {
        setError((solutions[0]));
        return;
    } else {
        setResults(solutions);
        setCurrentItem(0);
    }
}