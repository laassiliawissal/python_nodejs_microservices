const express = require('express');
const axios = require('axios'); // You'll need to install axios via npm

const app = express();

app.get('/', (req, res) => {
  // Make an API request to the backend
  axios.get('http://localhost:5000/api/message')
    .then(response => {
      res.send('Frontend received this message from the backend: ' + response.data);
    })
    .catch(error => {
      res.status(500).send('Error communicating with the backend.');
    });
});

app.listen(3000, () => {
  console.log('Frontend server is running on http://localhost:3000');
});