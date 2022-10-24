const Empleado = require('../models/empleados.model');

let response = {
    msg: "",
    exito: false
}

// Create and Save a new Empleado
exports.create = (req, res) => {
    // Validate request
    if (!req.body) {
        response.msg = "El contenido no puede estar vacío.";
        res.status(400).send(response);
    }

    // Create a Empleado
    const empleado = new Empleado({
        nombre: req.body.nombre,
        apellido_p: req.body.apellido_p,
        apellido_m: req.body.apellido_m,
        telefono: req.body.telefono,
        mail: req.body.mail,
        direccion: req.body.direccion
    });

    // Save Empleado in the database
    empleado
        .save(empleado)
        .then(data => {
            response.msg = "Empleado creado con éxito.";
            response.exito = true;
            res.send(response);
        })
        .catch(err => {
            response.msg = err.message || "Ocurrió un error al crear el empleado.";
            res.status(500).send(response);
        });
}

exports.find = function (req, res) {
    Empleado.find(function (err, empleados) {
        res.json(empleados)
    })
}

exports.findOne = function (req, res) {
    Empleado.findOne({ _id: req.params.id }, function (err, empleado) {
        res.json(empleado)
    })
}

exports.update = function (req, res) {
    let empleado = {
        nombre: req.body.nombre,
        apellido_p: req.body.apellido_p,
        apellido_m: req.body.apellido_m,
        telefono: req.body.telefono,
        mail: req.body.mail,
        direccion: req.body.direccion
    }

    Empleado.findByIdAndUpdate(req.params.id, { $set: empleado }, function (err) {
        if (err) {
            console.error(err),
                response.exito = false,
                response.msg = "Error al modificar el empleado"
            res.json(response)
            return;
        }

        response.exito = true,
            response.msg = "Empleado modifico correctamente"
        res.json(response)
    })
}

exports.remove = function (req, res) {
    Empleado.findByIdAndRemove({ _id: req.params.id }, function (err) {
        if (err) {
            console.error(err),
                response.exito = false,
                response.msg = "Error al eliminar el empleado"
            res.json(response)
            return;
        }

        response.exito = true,
            response.msg = "Empleado eliminado correctamente"
        res.json(response)
    })
}