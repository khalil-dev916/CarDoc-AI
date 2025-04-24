// test-server.js
import express from 'express';

const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Test server works!');
});

app.listen(port, () => {
  console.log(`Test server running at http://localhost:${port}`);
});

process.on('uncaughtException', err => {
  console.error('Uncaught Exception:', err);
});
process.on('unhandledRejection', reason => {
  console.error('Unhandled Rejection:', reason);
});