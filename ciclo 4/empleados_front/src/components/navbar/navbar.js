import React from 'react';
import { Container, Navbar, Nav, Dropdown, DropdownButton, Row } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUserAstronaut, faSignOut } from '@fortawesome/free-solid-svg-icons';
import './navbar.css';
export default class menu extends React.Component {
    constructor(props) {
        super(props);
        this.state = {};
    }
    state = {}
    render() {
        return (<Navbar id="navbar" bg="primary" expand="lg" variant="dark" fixed='top' >
            <Container>
                <Navbar.Brand id="navbar-title-css" href="#home">Novios.com <span id="usuario-sub-branm"></span> </Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        {/* <Nav.Link href="#home">Inicio</Nav.Link>
                        <Nav.Link href="#link">Perfil</Nav.Link> */}

                    </Nav>

                    <DropdownButton id="dropdown-basic-button" title="Usuario">
                        <Dropdown.Header id="dropdown-header">
                            <Row>
                                <FontAwesomeIcon icon={faUserAstronaut} />
                            </Row>
                            <Row>
                                #Usuario#
                            </Row>

                        </Dropdown.Header>

                        <Dropdown.Divider />

                        <Dropdown.Item href="#/action-1" id="cerrar-sesion"> <FontAwesomeIcon icon={faSignOut} /> Cerrar sesión</Dropdown.Item>
                        {/*  <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
                        <Dropdown.Item href="#/action-3">Something else</Dropdown.Item> */}
                    </DropdownButton>

                </Navbar.Collapse>
            </Container>
        </Navbar>);
    }
}