import React, { Component } from 'react';
import DocumentMeta from 'react-document-meta';

/* components */
import {EachPost} from '../../components/EachPost';

export class EachPostView extends Component {


    render() {
        return (
            <section>
                <EachPost/>
            </section>
        );
    }
}
