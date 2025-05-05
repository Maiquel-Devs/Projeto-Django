import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import ListaNomes from './Componenetes/ListaNomes';
import AdicionarNome from './Componenetes/AdicionarNome';

function App() {
  return (
    <Router>
      <nav>
        <Link to="/listar">Ver Lista</Link> | 
        <Link to="/adicionar">Adicionar Nome</Link>
      </nav>

      <Routes>
        <Route path="/listar" element={<ListaNomes />} />
        <Route path="/adicionar" element={<AdicionarNome />} />
      </Routes>
    </Router>
  );
}

export default App;
