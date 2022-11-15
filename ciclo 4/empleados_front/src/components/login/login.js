import React from 'react';
import axios from 'axios';
import { Container, Form, Button, Row, Col } from 'react-bootstrap';
import './login.css';
import { isNull } from 'util';
import Cookies from 'universal-cookie';
import app from '../../app.json';

const { APIHOST } = app;

export default class login extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            usuario: '',
            pass: ''
        };
    }

    iniciarSesion() {
        axios.post(`${APIHOST}/usuarios/login`, {
            usuario: this.state.usuario,
            pass: this.state.pass,
        }
        ).then((response) => {
            if (isNull(response.data.token)) {
                alert('usuario y/o contraseña invalidas');
            } else {

            }
            console.log(response.data.token);

        }).catch((err) => {
            console.log(err);
        });
    }

    render() {
        return (

            <Container className="login">
                <Container id="login-container">
                    <Row>
                        <Col>
                            <Row>
                                <h3>Iniciar sesión</h3>
                            </Row>

                            <Row>
                                <Col>
                                    <Form>
                                        <Form.Group >
                                            {/* <Form.Label >Usuario:</Form.Label> */}
                                            <Form.Control type="text" placeholder="Usuario" autoFocus onChange={(e) =>
                                                this.setState({ usuario: e.target.value })} />
                                        </Form.Group>

                                        <Form.Group >
                                            {/* <Form.Label >Contraseña:</Form.Label> */}
                                            <Form.Control type="password" placeholder="Contraseña" onChange={(e) =>
                                                this.setState({ pass: e.target.value })} />

                                        </Form.Group>

                                        <Button variant="primary"
                                            onClick={() => this.iniciarSesion()}>
                                            Entrar
                                        </Button>
                                    </Form>
                                </Col>
                            </Row>
                        </Col>
                    </Row>
                </Container>
            </Container>
        );
    }
}

