import React, { useEffect, useState } from 'react';
import axios from 'axios';

function ListaNomes() {
  const [nomes, setNomes] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/nomes/')
      .then(res => setNomes(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Lista de Nomes</h2>
      <ul>
        {nomes.map(nome => <li key={nome.id}>{nome.nome}</li>)}
      </ul>
    </div>
  );
}

export default ListaNomes;
