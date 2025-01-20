import { WordData } from "../types/WordDataTypes";

// TODO: FIX FORMATTING
// When wordData is selected for the first time, the formatting of the grid becomes evenly spaced instead of condensed in center
// remove the print statements and start writing function to highlight and connect the letters in the grid


export function WordGridDisplay({ wordData, gridSize, board } : {wordData: WordData | undefined, gridSize: number, board: string[][]}) {
    return (
        <div className="grid gap-0" style={{ gridTemplateColumns: `repeat(${gridSize}, 1fr)` }}>
                  
                  {board.map((row, i) =>
                    row.map((cell, j) => (
                      <input
                        key={`wg-${i}-${j}`}
                        id={`wg-${i}-${j}`}
                        type="text"
                        value={cell}
                        className="w-12 h-12 text-center border rounded-md uppercase text-lg"
                      />
                    ))
                  )}
            <div>
                {wordData && `${wordData.word}, ${wordData.rows}, ${wordData.cols}`}
            </div>
        </div>
        
    );
}