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

// Codigo de la profesora
/*
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
*/

