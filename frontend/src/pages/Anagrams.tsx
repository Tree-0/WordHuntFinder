import React, { useState, ChangeEvent } from 'react';
import {generateBoard, handleClearBoard, handleGridSizeChange, handleInputChange, handleSubmit } from '../util/helpers_anagrams';

const Anagrams: React.FC = () => {
    const [stringSize, setStringSize] = useState<number>(3);
    const [letters, setLetters] = useState<string[]>(generateBoard(stringSize));
    const [results, setResults] = useState<string[]>([]);
    const [error, setError] = useState<string>('');
    const [currentItem, setCurrentItem] = useState<number>(0);
    
    const MAX_ITEM_DISPLAY = 10;

    return (
        <div className="min-h-screen bg-gray-100 flex flex-col items-center p-6">

            <h1 className="text-4xl font-bold text-blue-600 mb-4">Wordhunt Solver</h1>
    
            {/* Grid Size Selector */}
            <div className="mb-6 flex gap-4">
            {[5, 6, 7].map((size) => (
                <button
                key={size}
                onClick={() => handleGridSizeChange(setLetters, setStringSize, letters, size)}
                className={`px-4 py-2 rounded-md ${stringSize === size ? 'bg-blue-600 text-white' : 'bg-gray-200'
                    }`}
                >
                {size}x{size}
                </button>
    
            ))}
            {/* Clear Board */}
            <button
                onClick={() => handleClearBoard(setLetters, stringSize)}
                className="bg-red-600 text-white px-4 py-2 rounded-md hover:bg-red-700"
            >
                Clear Board
            </button>
            </div>

            {/* Board Input */}
            <form
                onSubmit={(e) => handleSubmit(e, stringSize, letters, setResults, setError, setCurrentItem)}
                className="bg-white p-4 shadow-md rounded-md flex flex-col gap-4 w-full max-w-md"
                >
                <div className="grid gap-2" style={{ gridTemplateColumns: `repeat(${stringSize}, 1fr)` }}>
                    {letters.map((v, i) =>
                        <input
                        key={`${i}`}
                        type="text"
                        value={v}
                        onChange={(e: ChangeEvent<HTMLInputElement>) => handleInputChange(i, e.target.value, letters, setLetters)}
                        className="w-12 h-12 text-center border rounded-md uppercase text-lg"
                        />
                    )}
                </div>
        
                <button
                    type="submit"
                    className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700"
                >
                Solve
                </button>
            </form>

            {/* Error Message */}
            {error && <p className="text-red-500 mt-4">{error}</p>}

            {/* Results */}
            {
            results.length > 0 && (
                <div className="mt-6 w-full max-w-md">
                <h2 className="text-2xl font-bold mb-2">{results.length} Found Words:</h2>
                <ul className="bg-white p-4 shadow-md rounded-md">
                    {results.slice(currentItem, currentItem + MAX_ITEM_DISPLAY).map((word, index) => (
                    <li key={index} className="border-b last:border-none py-2">
                        {word}
                    </li>
                    ))}
                </ul>
                <div className="flex justify-between mt-4">
                    <button
                    onClick={() => setCurrentItem(Math.max(0, currentItem - MAX_ITEM_DISPLAY))}
                    disabled={currentItem === 0}
                    className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 disabled:opacity-50"
                    >
                    Previous
                    </button>
                    <button
                    onClick={() =>
                        setCurrentItem(
                        Math.min(currentItem + MAX_ITEM_DISPLAY, results.length - (results.length % MAX_ITEM_DISPLAY || MAX_ITEM_DISPLAY))
                        )
                    }
                    disabled={currentItem + MAX_ITEM_DISPLAY >= results.length}
                    className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 disabled:opacity-50"
                    >
                    Next
                    </button>
                </div>
                </div>
            )
            }
        </div>
        
    )
}

export default Anagrams;