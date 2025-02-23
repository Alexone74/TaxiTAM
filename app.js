// app.js
import React from 'react';
import { createRoot } from 'react-dom/client';
import { QuizApp } from './QuizApp.js';

const container = document.getElementById('root');
const root = createRoot(container);
root.render(React.createElement(QuizApp));