const express = require('express');
const app = express();
const PORT = 8080;

app.listen(PORT, () => {
    console.log(`Servidor corriendo en el puerto http://localhost:${PORT}`);
});

app.get('/tshirt', (req, res) => { // Added 'req' parameter
    res.status(200).send({
        tshirt: '👕',
        size: 'large'
    });
});

app.get('/shorts', (req, res) => { // Added 'req' parameter
    res.status(200).send({
        tshirt: '👖',
        size: 'medium'
    });
});

app.post('/tshirt/:id', (req, res) => {
    const { logo } = req.body;

    if (!logo) {
        res.status(418).send({ message: 'We need a logo!' });
    }
});


