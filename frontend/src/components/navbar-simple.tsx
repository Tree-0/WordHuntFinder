import { Link } from './link';
import { Button } from './button.tsx';

export function NavbarSimple() {
    return (
        <div style={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            gap: '1rem', // Adjust gap between buttons
            padding: '1rem', // Optional padding for better spacing
        }}>
            <Link href="/wordhunt">
                <Button>
                    Wordhunt
                </Button>
            </Link>
            <Link href="/anagrams">
                <Button>
                    Anagrams
                </Button>
            </Link>
        </div>
    );
}
