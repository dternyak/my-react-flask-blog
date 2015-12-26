import React, { Component } from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import Counter from '../../components/Counter/Counter';
import * as CounterActions from '../../actions/counter'

@connect(
    state => {
        return {counter: state.counter, state: state}
    },
    dispatch => bindActionCreators(CounterActions, dispatch)
)
export class CounterView extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <section>
                <div className="container">
                    <div className="row">
                        <div className="col-xs-12 col-sm-12 col-md-6 col-lg-6
                            col-md-offset-3 col-lg-offset-3">
                            <Counter {...this.props} />
                        </div>
                    </div>
                </div>
            </section>
        );
    }
}
