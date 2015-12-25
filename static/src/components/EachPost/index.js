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
        console.log("got here")
        console.log(this.props.id);

        get_single_post(data)
            .then((response) => {
                    console.log(response);
                    console.log(this.props.id);
                    //this.setState({
                    //    post: response.data,
                    //})
                }
            );

    }

    componentWillMount() {
        console.log("test")
    }

    render() {
        return (
            <div className="container">
                test {this.props.id}
            </div>

        )
    }

}
