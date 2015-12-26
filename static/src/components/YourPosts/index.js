import React, { Component } from 'react';

import styles from './clean-blog.css';

import {get_posts} from '../../utils/http_functions'

export class YourPosts extends Component {

    constructor(props) {
        super(props);
        this.state = {
            posts: []
        }
    }

    componentDidMount() {
        get_posts()
            .then((response) => {
                    console.log(response);
                    this.setState({
                        posts: response.data.data,
                    })
                }
            );

    }

    render() {
        return (
            <div className="container" style={styles}>
                <div className="container centered">
                    <h2><b>Blog Posts</b></h2>
                </div>
                <div className="row">
                    <div className="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
                        <div className="post-preview">
                            {
                                this.state.posts.map((post, index) =>
                                    <div key={index}>
                                        <a href={"#/post/" + post.id}>
                                            <h2 className="post-title">
                                                {post.title}
                                            </h2>
                                        </a>

                                        <p className="post-meta">Posted by {post.author } on {post.time}</p>
                                        <hr/>
                                    </div>
                                )
                            }
                        </div>
                    </div>
                </div>
            </div>

        )
    }


}
