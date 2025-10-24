import { useState } from 'react';
import { Card, Button, Form } from 'react-bootstrap';

function Login() {
  
  const [username, createUsername] = useState('');
  const [password, createPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    await fetch('http://localhost:5000/create', {
      method: 'POST',
      headers: { 'Content-Type' : 'application/json' },
      body: JSON.stringify({
        username: username,
        password: password 
      })
    })
  }
  
  return (
    <Card bg="light">
        <Card.Header>Banksie</Card.Header>
        <Card.Body>
          <Card.Title>Sign In</Card.Title>
          <Form>
            <Form.Group controlId='username'>
              <Form.Label>Username:</Form.Label>
              <Form.Control type='text'></Form.Control>
            </Form.Group>
            <Form.Group controlId='password'>
              <Form.Label>Password:</Form.Label>
              <Form.Control type='text'></Form.Control>
            </Form.Group>
            <Button type="submit">Sign In</Button>
          </Form>
          <Button>Create Account</Button>
        </Card.Body>
    </Card>
  )
}
export default Login;