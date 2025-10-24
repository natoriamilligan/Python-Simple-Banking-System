import './App.css';
import { Container } from 'react-bootstrap';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/login';

function App() {
  return (
    <Container fluid>
      <Router>
        <Routes>
          <Route path='/login' element={<Login />} />
        </Routes>
      </Router>
    </Container>
  );
}

export default App;
