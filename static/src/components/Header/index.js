import React, { Component } from 'react';
import { Link } from 'react-router';

/* component styles */

export class Header extends Component {
    constructor(props) {
        super(props);
    }


    render() {
        return (
            <header ref="header">

                <div className="logo">
                    <h2>DT</h2>
                </div>
            </header>
        );
    }
}
