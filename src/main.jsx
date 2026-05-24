import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './App.css'

const rootElement = document.getElementById('root');

if (!rootElement) {
  document.body.innerHTML = "<h1 style='color:red; text-align:center;'>Error: HTML missing 'root' div!</h1>";
} else {
  ReactDOM.createRoot(rootElement).render(
    <React.StrictMode>
      <App />
    </React.StrictMode>
  )
}
