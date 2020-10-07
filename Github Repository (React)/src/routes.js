import React from 'react';

import { BrowserRouter, Switch, Route } from 'react-router-dom';

import Main from './components/Main';
import Search from "./components/Search";

const Routes = () => (
    <BrowserRouter>
      <Switch>
        <Route exact path="/" component={Main} />
        <Route path ="/search" component={Search}/>
      </ Switch>
    </ BrowserRouter>
);

export default Routes;