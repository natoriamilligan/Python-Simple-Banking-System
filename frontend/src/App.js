import logo from './logo.svg';
import './App.css';
import { Container, Card, Form, Button } from 'react-bootstrap';

function App() {
  return (
    <Container fluid>
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
          </Form>
          <Button type="submit">Sign In</Button>
          <Button>Create Account</Button>
        </Card.Body>
      </Card>
    </Container>
  );
}

export default App;
