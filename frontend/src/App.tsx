// App.tsx
import { Routes, Route } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import WordHunt from "./pages/WordHunt"

const theme = createTheme({
  colorSchemes: {
    dark: true,
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Routes>
        <Route path="/" element={<WordHunt />} />
      </Routes>
    </ThemeProvider>
  );
}


export default App;
