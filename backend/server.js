// server.js
import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';

dotenv.config();
const app = express();
const port = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

const OPENROUTER_API_KEY = process.env.OPENROUTER_API_KEY;

async function queryOpenRouter(message) {
  const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${OPENROUTER_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/gpt-3.5-turbo',
      messages: [
        { role: 'system', content: 'You are a professional car mechanic assistant. Help users diagnose car problems based on their descriptions.' },
        { role: 'user', content: message }
      ]
    }),
  });

  const data = await response.json();
  console.log("OpenRouter Raw Response:", data);

  if (data && data.choices && data.choices.length > 0) {
    return data.choices[0].message.content.trim();
  } else {
    console.error('Unexpected OpenRouter response:', JSON.stringify(data));
    return "I'm not sure how to answer that right now.";
  }
}

// Backend API endpoint
app.post('/api/chat', async (req, res) => {
  const { message } = req.body;

  try {
    const reply = await queryOpenRouter(message);
    res.json({ reply });
  } catch (error) {
    console.error('Error querying OpenRouter:', error);
    res.status(500).send('Error connecting to AI model.');
  }
});

// Fallback endpoint for testing
app.get('/', (req, res) => {
  res.send('CarDoc AI backend is running.');
});

// Start server
app.listen(port, () => {
  console.log(`Backend server running at http://localhost:${port}`);
});

process.on('uncaughtException', err => {
  console.error('Uncaught Exception:', err);
});
process.on('unhandledRejection', reason => {
  console.error('Unhandled Rejection:', reason);
});
