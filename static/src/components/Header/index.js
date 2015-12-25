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
                <div className="container">
                    <div className="row">
                        <div className="col-xs-5 col-sm-3 col-md-3 col-lg-3 logo">
                            <Link to="/">
                                Redux Easy Boilerplate
                            </Link>
                        </div>


                        <div className="col-lg-8 hidden-xs text-right">
                            <nav>
                                <Link to="/home" activeClassName="active">
                                    Home
                                </Link>
                                <Link to="/list" activeClassName="active">
                                    Forms
                                </Link>
                                <Link to="/counter" activeClassName="active">
                                    Counter
                                </Link>
                            </nav>

                        </div>
                    </div>
                </div>
            </header>
        );
    }
}
