import React, { Component, PropTypes } from 'react'
import styles from './styles';

class Counter extends Component {
    render() {
        const { increment, incrementIfOdd, incrementAsync, decrement, counter } = this.props
        return (
            <div className={styles}>
                <p className="test">
                    Clicked: {counter} times
                    {' '}
                </p>
                <button type="button" className="btn btn-default" onClick={increment}>+</button>
                {' '}
                <button type="button" className="btn btn-default" onClick={decrement}>-</button>
                {' '}
                <button type="button" className="btn btn-default" onClick={incrementIfOdd}>Increment if odd</button>
                {' '}
                <button type="button" className="btn btn-default" onClick={() => incrementAsync(1000)}>Increment async
                </button>

            </div>
        )
    }
}

Counter.propTypes = {
    increment: PropTypes.func.isRequired,
    incrementIfOdd: PropTypes.func.isRequired,
    incrementAsync: PropTypes.func.isRequired,
    decrement: PropTypes.func.isRequired,
    counter: PropTypes.number.isRequired
}

export default Counter