import { useState } from 'react';
import { Card, Button, Form } from 'react-bootstrap';

function Create() {
    const [firstname, createFirstname] = useState('');
    const [lastname, createLastname] = useState('');
    const [username, createUsername] = useState('');
    const [password, createPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await fetch('http://localhost:5000/create', {
                method: 'POST',
                header: {'Content-Type' : 'application/json'},
                body: JSON.stringify({
                    first_name : firstname,
                    last_name : lastname,
                    username : username,
                    password : password
                })
            })
        } catch {
            alert("Something wrong with the server");
        }
    }

    return (
        <Card bg="light">
        <Card.Header>Banksie</Card.Header>
        <Card.Body>
          <Card.Title>Create Account</Card.Title>
          <Form onSubmit={handleSubmit}>
            <Form.Group controlId='firstname'>
              <Form.Label>First Name:</Form.Label>
              <Form.Control 
                type='text' 
                value={firstname}
                onChange={(e) => createFirstname(e.target.value)}
              />
            </Form.Group>
            <Form.Group controlId='lastname'>
              <Form.Label>Last Name:</Form.Label>
              <Form.Control 
                type='text' 
                value={lastname}
                onChange={(e) => createLastname(e.target.value)}
              />
            </Form.Group>
            <Form.Group controlId='username'>
              <Form.Label>Username:</Form.Label>
              <Form.Control 
                type='text' 
                value={username}
                onChange={(e) => createUsername(e.target.value)}
              />
            </Form.Group>
            <Form.Group controlId='password'>
              <Form.Label>Password:</Form.Label>
              <Form.Control 
                type='text' 
                value={password}
                onChange={(e) => createPassword(e.target.value)}
              />
            </Form.Group>
            <Button type='submit'>Create Account</Button>
          </Form>
        </Card.Body>
    </Card>
    )
};
export default Create;
