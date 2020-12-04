import React from 'react';
import {Link} from 'react-router-dom';
import Logo from './grab-logo.png';
import './App.css';

function Home() {
  return (
    <div>
      <img src={Logo} alt='logo' className="homeImage"></img>
      <h1 className="logoText">serwis internetowy</h1>
      <h3></h3>
      <Link to="/shop" className="shopLink">Zobacz Naszą ofertę</Link>

    </div>
  );
}

export default Home;