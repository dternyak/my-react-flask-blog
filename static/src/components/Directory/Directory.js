import React, { Component, PropTypes } from 'react'
import { Link } from 'react-router';

class Directory extends Component {
    render() {
        return (
            <div id="h">
                <div className="container centered">
                    <div className="row">
                        <div className="col-md-8 col-md-offset-2">
                            <h1>Hello, my name is <b>Daniel Ternyak</b>.<br/>I create web applications with
                                <b> Python</b> and <b>Javascript</b> on the <b>Cloud.</b></h1>
                        </div>
                    </div>
                    <div className="row mt">
                        <div className="col-sm-4">

                            <i className="ion-monitor"/>
                            <Link to="/portfolio" activeClassName="active">

                                <h3>Portfolio</h3>
                            </Link>
                        </div>

                        <div className="col-sm-4">
                            <i className="ion-ios-bookmarks-outline"/>
                            <h3>Blog</h3>
                        </div>

                        <div className="col-sm-4">
                            <i className="ion-ios-paper-outline"/>
                            <a target="_blank" href="https://drive.google.com/file/d/0B3hYpsXRDCIkMWt1T3lPMkZ4MkE/view">

                                <h3>Rèsumè</h3>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}


export default Directory