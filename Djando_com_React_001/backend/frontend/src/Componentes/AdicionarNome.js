import React, { useState } from 'react';
import axios from 'axios';

function AdicionarNome() {
  const [nome, setNome] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post('http://localhost:8000/api/nomes/', { nome });
    setNome("");
  };

  return (
    <div>
      <h2>Adicionar Nome</h2>
      <form onSubmit={handleSubmit}>
        <input value={nome} onChange={e => setNome(e.target.value)} required />
        <button type="submit">Salvar</button>
      </form>
    </div>
  );
}

export default AdicionarNome;
