import axios from 'axios'


export function get_posts() {
    return axios.get('/api/v1/your_posts')
}


export function get_single_post(post) {
    return axios.post('/api/v1/get_single_post', {
            id: post
        }
    )
}

export function create_post(title, body) {
    return axios.post('/api/v1/create_post', {
            title: title,
            body: body
        }
    )
}