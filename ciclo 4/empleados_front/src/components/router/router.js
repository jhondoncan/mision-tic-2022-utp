import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from '../login/login';
import Inicio from '../index/index';


export default function AppRoutes() {
    return (
        <Router>
            <Routes>
                <Route exact path="/login" element={<Login />} />
                <Route path="/*" element={(
                    <h1 style={{ marginTop: 300, fontSize: 60 }}> 404 <br />¡Oh no!, Página no encontrada</h1>
                )} />
                <Route exact path="/" element={<Inicio />} />
                <Route exact path="/index" element={<Inicio />} />
            </Routes>
        </Router >
    );
}

