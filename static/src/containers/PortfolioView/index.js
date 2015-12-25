import React, { Component } from 'react';
import DocumentMeta from 'react-document-meta';

/* components */
import Portfolio from '../../components/Portfolio/Portfolio';

export class PortfolioView extends Component {
    render() {
        return (
            <section>
                <Portfolio/>
            </section>
        );
    }
}
