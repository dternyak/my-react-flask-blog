import React, { Component } from 'react';
import DocumentMeta from 'react-document-meta';

/* components */
import {YourPosts} from '../../components/YourPosts';


export class BlogView extends Component {
    render() {
        return (
            <section>
                <YourPosts/>
            </section>
        );
    }
}
