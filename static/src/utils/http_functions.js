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