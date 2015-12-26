import React, { Component } from 'react';

import {get_single_post} from '../../utils/http_functions'

export class EachPost extends Component {

    constructor(props) {
        super(props);
        this.state = {
            post: [],
        }
    }

    componentDidMount() {
        console.log(this.props.id);

        get_single_post(this.props.id)
            .then((response) => {
                    response.data.data.body = {__html: response.data.data.body};
                    this.setState({
                        post: response.data.data,
                    })
                }
            );
    }

    render() {
        const post = this.state.post;
        return (
            <div className="container">
                <div className="row">
                    <div className="col-lg-8">
                        <h1>{post.title}</h1>

                        <p className="lead">
                            by: {post.author}
                        </p>
                        <hr/>
                        <p> Posted on {post.time} </p>
                        <hr/>
                        <div dangerouslySetInnerHTML={post.body}></div>
                    </div>
                </div>


            </div>


        )
    }

}
