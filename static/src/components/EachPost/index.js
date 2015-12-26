import React, { Component } from 'react';

import {get_single_post} from '../../utils/http_functions'

export class EachPost extends Component {

    constructor(props) {
        super(props);
        this.state = {
            post: []
        }
    }

    componentDidMount() {
        console.log(this.props.id);

        get_single_post(this.props.id)
            .then((response) => {
                    console.log(response);
                    //this.setState({
                    //    post: response.data,
                    //})
                }
            );
     }
    render() {
        return (
            <div className="container">
                test
            </div>

        )
    }

}
