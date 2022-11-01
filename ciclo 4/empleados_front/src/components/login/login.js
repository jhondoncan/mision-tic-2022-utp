import React from 'react';
import { Container, Form, Button, Row, Col } from 'react-bootstrap';
import './login.css';

export default class login extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            usuario: '',
            pass: ''
        };
    }

    iniciarSesion() {
        alert(`Usuario: ${this.state.usuario} - Contraseña: ${this.state.pass}`);
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
                                <Col

                                >
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

                                        <Button variant="primary" type="submit"
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

