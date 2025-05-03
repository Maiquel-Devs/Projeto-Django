import './App.css';

//Link
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

//Componentes
import AdicionarNome from './Componentes/AdicionarNome';
import VerNomes from './Componentes/VerNomes';

function App() {
  return (
    <Router>
      <nav>
        <Link to="/adicionar">Adicionar Nome</Link> | <Link to="/ver">Ver Nomes</Link>
      </nav>
      <Routes>
        <Route path="/adicionar" element={<AdicionarNome />} />
        <Route path="/ver" element={<VerNomes />} />
      </Routes>
    </Router>
  );
}

export default App;