import React, { Component } from 'react';
import DocumentMeta from 'react-document-meta';

/* components */
//import { TopImage } from 'components/TopImage';
//import { Tools } from 'components/Tools';
//import { Projects } from 'components/Projects';



const metaData = {
    title: 'Redux Easy Boilerplate',
    description: 'Start you project easy and fast with modern tools',
    canonical: 'http://example.com/path/to/page',
    meta: {
        charset: 'utf-8',
        name: {
            keywords: 'react,meta,document,html,tags',
        },
    },
};

export class Home extends Component {
    render() {
        return (
            <section>
                <div id="h">
                    <div className="container centered">
                        <div className="row">
                            <div className="col-md-8 col-md-offset-2">
                                <h1>Hello, my name is <b>Daniel White</b>.<br/>I create for the web.</h1>
                            </div>
                        </div>
                        <div className="row mt">
                            <div className="col-sm-4">
                                <i className="ion-monitor"/>
                                <h3>Web Design</h3>
                            </div>

                            <div className="col-sm-4">
                                <i className="ion-ios-bookmarks-outline"/>
                                <h3>UI Development</h3>
                            </div>

                            <div className="col-sm-4">
                                <i className="ion-ios-paper-outline"/>
                                <h3>Brand Identity</h3>
                            </div>
                        </div>
                    </div>
                </div>

            </section>
        );
    }
}
