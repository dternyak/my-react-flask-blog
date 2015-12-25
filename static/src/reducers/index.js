import { combineReducers } from 'redux';
import { routeReducer } from 'redux-simple-router';
import { reducer as formReducer } from 'redux-form';
import { items } from './items';
import {counter} from './counter'

const rootReducer = combineReducers({
    form: formReducer,
    routing: routeReducer,
    /* your reducers */
    counter: counter,
    items,
});

export default rootReducer;
