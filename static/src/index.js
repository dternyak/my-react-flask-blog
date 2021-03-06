import React from 'react';
import ReactDOM from 'react-dom';
import createHistory from 'history/lib/createHashHistory';
import { Provider } from 'react-redux';
import { Router, Redirect } from 'react-router';
import configureStore from './store/configureStore';
import routes from './routes';
import { syncReduxAndRouter } from 'redux-simple-router';

const store = configureStore();

import 'css/style.css'
import 'css/loading.css'


const history = createHistory();

syncReduxAndRouter(history, store);

ReactDOM.render(
    <Provider store={store}>
        <Router history={history}>
            <Redirect from="/" to="home"/>
            {routes}
        </Router>
    </Provider>,
    document.getElementById('root')
);
