import axios from 'axios'


export function get_posts() {
    return axios.get('/api/v1/your_posts')
}