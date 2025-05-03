import React, { useEffect, useState } from 'react';
import axios from 'axios';

function VerNomes() {
  const [nomes, setNomes] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/nomes/')
      .then(res => setNomes(res.data));
  }, []);

  return (
    <div>
      <h2>Lista de Nomes</h2>
      <ul>
        {nomes.map(n => (
          <li key={n.id}>{n.nome}</li>
        ))}
      </ul>
    </div>
  );
}

export default VerNomes;

