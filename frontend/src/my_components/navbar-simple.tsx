import { Link } from 'react-router-dom';
// import { Button } from '../components/button.tsx';

export function NavbarSimple() {
    return (
        <div style={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            gap: '1rem', // Adjust gap between buttons
            padding: '1rem', // Optional padding for better spacing
        }}>
            <Link to="/wordhunt">
                <button>
                    Wordhunt
                </button>
            </Link>
            <Link to="/anagrams">
                <button>
                    Anagrams
                </button>
            </Link>
        </div>
    );
}
