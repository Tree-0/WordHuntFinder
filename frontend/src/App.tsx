// App.tsx
import { Routes, Route } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import WordHunt from "./pages/WordHunt";
import Anagrams from "./pages/Anagrams";
import { NavbarSimple as Navbar } from './components/navbar-simple';

const theme = createTheme({
  colorSchemes: {
    dark: true,
  },
});

function App() {
  return (
    <div>
      
    <ThemeProvider theme={theme}>
        <h1 className="text-4xl font-bold text-blue-600 mb-4" style={{
          textAlign: 'center',
        }}>
          Word Game Solver</h1>
        <Navbar/>
          
        <Routes>
          <Route path="/"/>
          <Route path="/wordhunt" element={<WordHunt />} />
          <Route path="/anagrams" element={<Anagrams />} />
        </Routes>
      
    </ThemeProvider>
    </div>
    
  );
}


export default App;
