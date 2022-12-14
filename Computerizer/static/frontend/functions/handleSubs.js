/* Global Variables */
const absURL = 'http://127.0.0.1:8000' // website domain URL 
const baseURL = '/TPA/subscribe'

export const PostSubs = async (data = {}) => {
    const res = await fetch(absURL + baseURL, {
    method: 'POST', 
    credentials: 'same-origin',
    headers: {
        'Content-Type': 'application/json',
    },      
    body: JSON.stringify(data), 
    });

    try {
    const state = await res.json();
    return state;
    } catch(error) {
    console.log("error", error);
    }
}