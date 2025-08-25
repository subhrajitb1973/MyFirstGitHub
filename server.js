const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

let posts = [];

app.get('/api/categories', (req, res) => {
  const categories = [...new Set(posts.map(p => p.category))];
  res.json(categories);
});

app.get('/api/posts', (req, res) => {
  const { category } = req.query;
  if (category) {
    res.json(posts.filter(p => p.category === category));
  } else {
    res.json(posts);
  }
});

app.post('/api/posts', (req, res) => {
  const { title, category, content } = req.body;
  if (!title || !category || !content) {
    return res.status(400).json({ error: 'Missing fields' });
  }
  const id = posts.length + 1;
  const post = { id, title, category, content };
  posts.push(post);
  res.status(201).json(post);
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
