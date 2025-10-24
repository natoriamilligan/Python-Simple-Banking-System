import { useState } from 'react';
import { Card, Button, Form } from 'react-bootstrap';

function Logout() {
    return (
        <Card>
            <Card.Header bg="light">Banksie</Card.Header>
            <Card.Body>
                <Card.Text>You have been successfully logged out.</Card.Text>
            </Card.Body>
        </Card>
    )
}
export default Logout