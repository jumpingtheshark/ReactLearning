import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import  {createBrowserHistory} from 'history'


import App from './components/App'
import Jokes from './components/Jokes'
import './index.css'
import Header from "./components/Header";
//import {useLocation} from "react-router-dom";

//const history = createBrowserHistory();

ReactDOM.render(
    <Router history={createBrowserHistory()}>
        <Switch>
            <Route  path='/'  exact={true}   render = {()=><Header><App/></Header>}/>
            <Route path = '/jokes'   render={() => <Header><Jokes/></Header>  }/>
        </Switch>
    </Router>,
    document.getElementById("root")
        );
























