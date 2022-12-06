// async function getUsers() {
//     const res = await axios.get('https://reqres.in/api/users');
//     console.log(res)
// }

// async function createUsers() {
//     const res = await axios.post('https://reqres.in/api/users', { username: 'Butters', email: 'butters@gmail', age: 1 });
//     console.log(res);
// }

// createUsers();



async function getUsers(token) {
    const res = await axios.get('https://hack-or-snooze-v3.herokuapp.com/users', { params: { token } });
    console.log(res)
}

async function signUp(username, password, name) {
    const res = await axios.post('https://hack-or-snooze-v3.herokuapp.com/signup', { user: { name, username, password } })
    console.log(res);
}

async function logIn(username, password) {
    const res = await axios.post('https://hack-or-snooze-v3.herokuapp.com/login', { user: { username, password } })
    console.log(res);
    return res.data.token;
}

// eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IkJ1dHRlcnNJc2FDaGlja2VuIiwiaWF0IjoxNjcwMjgzMTI4fQ.4n0p41P3NflHLhBLj9wvHqKvh4dW9FQTeid54FHzMZU

// signUp('ButtersIsaChicken', 'peeword', 'Butters');

async function getUsersWithAuth() {
    const token = await logIn('ButtersIsaChicken', 'peeword');
    getUsers(token);
}

async function createStory() {
    const token = await logIn('ButtersIsaChicken', 'peeword');
    const newStory = {
        token,
        story: {
            author: 'Butters',
            title: 'I am Butters',
            url: "http://butters.com"
        }
    }
    const res = await axios.post('https://hack-or-snooze-v3.herokuapp.com/stories', newStory);
    console.log(res)
}

createStory()

// getUsersWithAuth()
