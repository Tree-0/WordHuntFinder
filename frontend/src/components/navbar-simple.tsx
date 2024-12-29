import { Link } from './link'

export function NavbarSimple()
{
    return (
    <div>
        <Link href="/wordhunt">
            <button>
                Wordhunt
            </button>
        </Link>
        <Link href="/anagrams">
            <button>
                Anagrams
            </button>
        </Link>
    </div>
    );
}