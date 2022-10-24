const moongose = require('mongoose');
const Schema = moongose.Schema;

const NoviosSchema = new Schema({
    id_novio: { type: String, required: true, max: 60 },
    nombre: { type: String, required: true, max: 60 },
    ciudad: { type: String, required: true, max: 60 },
    estatura: { type: Number, required: true, max: 300 },
    telefono: { type: String, required: true, max: 15 },
    contextura: { type: String, required: true, max: 100 },
    edad: { type: Number, required: true, max: 70 },
});

module.exports = moongose.model("novios", NoviosSchema); 