import Link from 'next/link';
import { useRouter } from 'next/router';
import styles from '@/styles/Navbar.module.css';

const Navbar = () => {
    const router = useRouter();

    return (
        <nav className={styles.navbar}>
            <div className={styles.logo}>
                <Link href="/">
                    <img src="/RFA_logo.png" alt="RFA Logo" width={50} height={50} />
                </Link>
            </div>
            <ul className={styles.navLinks}>
                <li className={router.pathname === "/parts" ? styles.active : ""}>
                    <Link href="/parts">Parts</Link>
                </li>
                <li className={router.pathname === "/users" ? styles.active : ""}>
                    <Link href="/users">Users</Link>
                </li>
            </ul>
        </nav>
    );
};

export default Navbar;
