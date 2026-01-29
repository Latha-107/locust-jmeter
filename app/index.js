const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to log incoming requests
app.use((req, res, next) => {
    console.log(`[${new Date().toISOString()}] ${req.method} ${req.path}`);
    next();
});

// Health check endpoint
app.get('/health', (req, res) => {
    res.status(200).json({ 
        status: 'healthy', 
        timestamp: new Date().toISOString() 
    });
});

// Root route
app.get('/', (req, res) => {
    res.status(200).json({
        message: 'Application is running',
        endpoints: ['/health', '/testing-load'],
        version: '1.0.0'
    });
});

// Testing load route
app.get('/testing-load', (req, res) => {
    res.status(200).json({
        message: 'Testing Load route is working!',
        timestamp: new Date().toISOString()
    });
});

// 404 handler for undefined routes
app.use((req, res) => {
    res.status(404).json({
        error: 'Not Found',
        path: req.path,
        message: `Cannot ${req.method} ${req.path}`
    });
});

// Error handler
app.use((err, req, res, next) => {
    console.error(`Error: ${err.message}`);
    res.status(500).json({
        error: 'Internal Server Error',
        message: err.message
    });
});

app.listen(PORT, () => {
    console.log(`App running on port ${PORT}`);
    console.log(`Environment: ${process.env.NODE_ENV || 'development'}`);
});
