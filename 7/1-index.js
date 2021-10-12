import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import  {createBrowserHistory} from 'history'


import App from './components/App'
import Jokes from './components/Jokes'
import './index.css'
//import {useLocation} from "react-router-dom";

//const history = createBrowserHistory();

ReactDOM.render(
    <Router history={createBrowserHistory()}>
        <nav>
            <ul>
                <li>
                    <Link to="/">Home</Link>
                </li>
                <li>
                    <Link to="/jokes">jokes</Link>
                </li>
            </ul>
        </nav>
        <Switch>
            <Route  path='/'  exact   component={App}/>
            <Route path = '/jokes'  component={Jokes}></Route>
        </Switch>
    </Router>,
    document.getElementById("root")
        );




