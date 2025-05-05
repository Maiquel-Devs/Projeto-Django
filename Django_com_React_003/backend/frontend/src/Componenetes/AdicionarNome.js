import React, { useState } from 'react';
import axios from 'axios';

function AdicionarNome() {
  const [nome, setNome] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://localhost:8000/api/nomes/', { nome })
      .then(() => {
        alert('Nome adicionado com sucesso!');
        setNome('');
      })
      .catch(err => console.error(err));
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>Nome:</label>
      <input value={nome} onChange={e => setNome(e.target.value)} required />
      <button type="submit">Salvar</button>
    </form>
  );
}

export default AdicionarNome;
