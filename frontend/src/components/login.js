import { useState } from 'react';
import { Card, Button, Form } from 'react-bootstrap';

function Login() {
  
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: { 'Content-Type' : 'application/json' },
        body: JSON.stringify({
          username: username,
          password: password 
        })
      })

      if (response.ok) {
        const data = await response.json();
        localStorage.setItem("accessToken", data.access_token)
        alert(data.access_token)
      } else {
        alert("Login unsuccessful")
      }
      
    } catch {
      alert("Something wrong with the server");
    }
  }
  
  return (
    <Card bg="light">
        <Card.Header>Banksie</Card.Header>
        <Card.Body>
          <Card.Title>Sign In</Card.Title>
          <Form onSubmit={handleSubmit}>
            <Form.Group controlId='username'>
              <Form.Label>Username:</Form.Label>
              <Form.Control 
                type='text' 
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
            </Form.Group>
            <Form.Group controlId='password'>
              <Form.Label>Password:</Form.Label>
              <Form.Control 
                type='text' 
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </Form.Group>
            <Button type="submit">Sign In</Button>
          </Form>
          <Button>Create Account</Button>
        </Card.Body>
    </Card>
  )
}
export default Login;