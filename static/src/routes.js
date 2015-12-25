import React from 'react';
import { Route } from 'react-router';

/* containers */
import { App } from 'containers/App';
import { Home } from 'containers/Home';
import { List } from 'containers/List';
import {CounterView} from 'containers/Counter'

export default (
    <Route path="/" component={App}>
        <Route path="home" component={Home}/>
        <Route path="list" component={List}/>
        <Route path="counter" component={CounterView}/>

    </Route>
);
