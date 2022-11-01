/* Funcion que conecta base de datos mongoose */
const mongoose = require("mongoose");

const host = "localhost";
const port = "27017";
const db = "hr";

exports.mongoConnect = () => {
    const mongoStringConnection = `mongodb://${host}:${port}/${db}`;
    /* const mongoStringConnection = "mongodb+srv://doncan:Gatito3312@doncan.bo1buja.mongodb.net/hv"; */
    mongoose.connect(mongoStringConnection);
    mongoose.Promise = global.Promise;
    const dbConnection = mongoose.connection;
    dbConnection.on("error", console.error.bind(console, "Mongodb connection error"))
}

