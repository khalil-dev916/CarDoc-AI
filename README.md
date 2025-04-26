# CarDoc AI - Intelligent Car Diagnostics Assistant

An AI-powered car diagnostic chat application that helps users identify and understand vehicle problems through natural language conversation.

## Features

- **AI-Powered Diagnostics** - Uses GPT-3.5 Turbo via OpenRouter for intelligent car troubleshooting
- **Modern Chat Interface** - Clean, responsive UI with message history, typing indicators, and timestamps
- **Quick Start Suggestions** - Pre-defined common car problems for instant testing
- **Real-time Communication** - Seamless frontend-backend integration
- **Dark Theme** - Professional automotive-inspired design with animated gradients

## Tech Stack

### Frontend
- **React 19** + **Vite 6** - Fast development and building
- **Vanilla CSS** - Custom modern styling with CSS variables
- **ES Modules** - Modern JavaScript module system

### Backend
- **Node.js** + **Express 4** - REST API server
- **OpenRouter API** - Access to multiple AI models
- **dotenv** - Environment configuration
- **CORS** - Cross-origin resource sharing

## Project Structure

```
website/
├── backend/
│   ├── server.js          # Express API server
│   ├── package.json
│   └── .env               # OPENROUTER_API_KEY
│
└── frontend/
    └── cardoc-ai/
        └── app/
            ├── src/
            │   ├── App.jsx        # Main chat component
            │   ├── App.css        # Complete styling
            │   ├── main.jsx       # Entry point
            │   └── index.css      # Global styles
            ├── public/
            │   └── car.svg        # Custom logo/favicon
            ├── package.json
            └── vite.config.js
```

## Prerequisites

- **Node.js 18+** (for ES modules and fetch API)
- **OpenRouter API Key** - Get one at [openrouter.ai](https://openrouter.ai)

## Setup Instructions

### 1. Backend Setup

```bash
cd backend
npm install
```

Create `.env` file in the backend directory:
```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

Start the backend server:
```bash
node server.js
```
Server runs at `http://localhost:3000`

### 2. Frontend Setup

```bash
cd frontend/cardoc-ai/app
npm install
```

Start the development server:
```bash
npm run dev
```
Frontend runs at `http://localhost:5173`

## Usage

1. Open `http://localhost:5173` in your browser
2. Click a suggestion button or type your car problem
3. Press Enter or click Send
4. CarDoc AI will provide diagnostic guidance

### Example Queries
- "My car makes a clicking noise when I turn the key"
- "Engine overheating after 30 minutes of driving"
- "Brake squealing when I press the pedal"
- "Check engine light is on, car runs rough"

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/chat` | Send message to AI, get diagnostic response |
| GET | `/` | Health check endpoint |

### Chat Request
```json
{
  "message": "Your car problem description"
}
```

### Chat Response
```json
{
  "reply": "AI diagnostic response"
}
```

## Configuration

### Change AI Model
Edit `backend/server.js` line 23:
```javascript
model: 'openai/gpt-3.5-turbo'  // Change to any OpenRouter model
```

Popular alternatives:
- `openai/gpt-4` - More capable
- `anthropic/claude-3-sonnet` - Excellent reasoning
- `meta-llama/llama-3-70b-instruct` - Open source
- `google/gemini-pro` - Google's model

### Customize System Prompt
Edit the system message in `backend/server.js` lines 25-26 to modify AI behavior.

## Development

### Frontend Hot Reload
Vite provides instant HMR (Hot Module Replacement) during development.

### Backend Auto-restart
For development, install nodemon:
```bash
cd backend
npm install -D nodemon
npx nodemon server.js
```

## Building for Production

### Frontend
```bash
cd frontend/cardoc-ai/app
npm run build
```
Output in `dist/` folder.

### Backend
No build step required. Set `NODE_ENV=production` and run:
```bash
node server.js
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENROUTER_API_KEY` | Your OpenRouter API key | Yes |
| `PORT` | Backend port (default: 3000) | No |

## Troubleshooting

### "AI not responding"
- Verify backend is running on port 3000
- Check OpenRouter API key is valid
- Check browser console for CORS errors

### Port already in use
```bash
# Kill existing Node processes
taskkill /F /IM node.exe
```

### Frontend not loading
- Ensure Vite dev server is running (`npm run dev`)
- Check port 5173 is available
- Try `http://192.168.1.13:5173` (network IP)

## License

MIT License - Feel free to use and modify for your projects.

## Acknowledgments

- [OpenRouter](https://openrouter.ai) for unified AI model access
- [Vite](https://vitejs.dev) for lightning-fast development
- [Express](https://expressjs.com) for minimal backend framework