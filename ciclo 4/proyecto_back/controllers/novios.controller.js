const Novio = require('../models/novios.model');

let response = {
    msg: "",
    exito: false
}

// Create and Save a new Novio
exports.create = (req, res) => {
    // Validate request
    if (!req.body) {
        response.msg = "El contenido no puede estar vacío.";
        res.status(400).send(response);
    }

    // Create a Novio
    const novio = new Novio({
        id_novio: req.body.id_novio,
        nombre: req.body.nombre,
        ciudad: req.body.ciudad,
        estatura: req.body.estatura,
        telefono: req.body.telefono,
        contextura: req.body.contextura,
        edad: req.body.edad
    });

    // Save Novio in the database
    novio.save(novio).then(data => {
        response.msg = "Novio creado con éxito.";
        response.exito = true;
        res.send(response);
    })
        .catch(err => {
            response.msg = err.message || "Ocurrió un error al crear el novio.";
            res.status(500).send(response);
        });
}

exports.find = function (req, res) {
    Novio.find(function (err, novios) {
        res.json(novios)
    })
}

exports.findOne = function (req, res) {
    Novio.findOne({ _id: req.params.id }, function (err, novio) {
        res.json(novio)
    })
}

exports.update = function (req, res) {
    let novio = {
        id_novio: req.body.id_novio,
        nombre: req.body.nombre,
        ciudad: req.body.ciudad,
        estatura: req.body.estatura,
        telefono: req.body.telefono,
        contextura: req.body.contextura,
        edad: req.body.edad
    }

    Novio.findByIdAndUpdate(req.params.id, { $set: novio }, function (err) {
        if (err) {
            console.error(err),
                response.exito = false,
                response.msg = "Error al modificar el novio"
            res.json(response)
            return;
        }

        response.exito = true,
            response.msg = "Novio modifico correctamente"
        res.json(response)
    })
}

exports.remove = function (req, res) {
    Novio.findByIdAndRemove({ _id: req.params.id }, function (err) {
        if (err) {
            console.error(err),
                response.exito = false,
                response.msg = "Error al eliminar el novio"
            res.json(response)
            return;
        }

        response.exito = true,
            response.msg = "Novio eliminado correctamente"
        res.json(response)
    })
}