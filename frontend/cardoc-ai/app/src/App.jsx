import { useState, useRef, useEffect } from 'react';
import './App.css';
import carLogo from './assets/car.svg';

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  async function sendMessage() {
    if (!input.trim() || isLoading) return;

    const userMessage = input.trim();
    setInput('');
    setIsLoading(true);

    // Add user message
    const newMessages = [...messages, { role: 'user', content: userMessage, timestamp: Date.now() }];
    setMessages(newMessages);

    try {
      const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:3000';
      const res = await fetch(`${API_URL}/api/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userMessage }),
      });

      const data = await res.json();
      setMessages([...newMessages, { role: 'bot', content: data.reply, timestamp: Date.now() }]);
    } catch (error) {
      setMessages([...newMessages, { role: 'bot', content: 'Connection error. Please check if the backend is running.', timestamp: Date.now() }]);
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <div className="app-container">
      <div className="card">
        <header className="header">
          <div className="logo-wrapper">
            <img src={carLogo} alt="CarDoc AI Logo" className="logo" />
          </div>
          <div className="header-text">
            <h1>CarDoc AI</h1>
            <p className="tagline">Intelligent Car Diagnostics</p>
          </div>
        </header>

        <div className="chat-container">
          <div className="chat-box" ref={messagesEndRef}>
            {messages.length === 0 && (
              <div className="welcome-message">
                <div className="welcome-icon">🚗</div>
                <h3>Welcome to CarDoc AI</h3>
                <p>Describe your car problem and I'll help you diagnose it</p>
                <div className="suggestions">
                  <button className="suggestion-btn" onClick={() => setInput("My car makes a clicking noise when I turn the key")}>
                    Clicking noise on startup
                  </button>
                  <button className="suggestion-btn" onClick={() => setInput("Engine overheating after 30 minutes of driving")}>
                    Engine overheating
                  </button>
                  <button className="suggestion-btn" onClick={() => setInput("Brake squealing when I press the pedal")}>
                    Brake squealing
                  </button>
                  <button className="suggestion-btn" onClick={() => setInput("Check engine light is on, car runs rough")}>
                    Check engine light
                  </button>
                </div>
              </div>
            )}
            {messages.map((msg, idx) => (
              <div key={idx} className={`message ${msg.role}`}>
                <div className="message-avatar">
                  {msg.role === 'user' ? '👤' : '🤖'}
                </div>
                <div className="message-content">
                  <div className="message-header">
                    <span className="message-sender">{msg.role === 'user' ? 'You' : 'CarDoc AI'}</span>
                    <span className="message-time">
                      {new Date(msg.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                    </span>
                  </div>
                  <div className="message-text">{msg.content}</div>
                </div>
              </div>
            ))}
            {isLoading && (
              <div className="message bot loading">
                <div className="message-avatar">🤖</div>
                <div className="message-content">
                  <div className="typing-indicator">
                    <span></span><span></span><span></span>
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>
        </div>

        <div className="input-area">
          <form onSubmit={(e) => { e.preventDefault(); sendMessage(); }}>
            <div className="input-wrapper">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={(e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); }}}
                placeholder="Describe your car problem..."
                className="message-input"
                disabled={isLoading}
                autoFocus
              />
              <button type="submit" className="send-btn" disabled={!input.trim() || isLoading}>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                  <line x1="22" y1="2" x2="11" y2="13"></line>
                  <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                </svg>
              </button>
            </div>
          </form>
          <p className="hint">Press Enter to send • Shift+Enter for new line</p>
        </div>
      </div>
    </div>
  );
}

export default App;