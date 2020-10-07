import React from 'react';

import './App.css';

import Title from './components/Title'
import Routes from "./routes";
import Footer from './components/Footer';

const App = () => (
    <div className="App">
        <Title/>
        <Routes/>
        <Footer/>
    </div>
);

export default App;
