import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import FundsList from './components/FundsList';
import HistoryList from './components/HistoryList';

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div className="min-h-screen bg-gray-50 p-8">
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-r from-blue-500 to-purple-500">
      <h1 className="text-5xl font-extrabold text-white">
        ¡TailwindCSS Funciona!
      </h1>
    </div>
      <h1 className="text-4xl font-bold text-center text-blue-600 mb-8">Plataforma de Fondos de Inversión</h1>
      
      <div  className="grid md:grid-cols-2 gap-10">
        <FundsList />
        <hr />
        <HistoryList />
      </div>
    </>
  )
}

export default App
