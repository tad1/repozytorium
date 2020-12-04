import React from 'react';
import './App.css';

function About() {
  return (
    <div>
      <h1 className="aboutName">O Nas</h1>
      <p className="about"> Jesteśmy sklepem sprzedającym przeróżne rzeczy: od Sprzętu Ogrodowego do Elektroniki.</p>
      <br></br>
      <br></br>
      <h2 className="contactInfoName">Kontakt:</h2>
      <div className="contactInfo">
        <h3>tel: +00 000 000 000</h3>
        <h3>email: info@grab.pl</h3>
      </div>
    </div>
  );
}

export default About;