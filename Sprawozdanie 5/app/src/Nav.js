import React from 'react';
import {Link} from 'react-router-dom';
import './App.css';
import Logo from './grab-logo.png';

function Nav() {

  return (
    <nav>
        <Link to="/"><img src={Logo} alt="logo" className="logo"/></Link>
        <ul className="nav-links">
            <Link to='/about' >
            <li>O Nas</li>
            </Link>
            <Link to='/shop'>
            <li>Sklep</li>
            </Link>
        </ul>
    </nav>
  );
}

export default Nav;