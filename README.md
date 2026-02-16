# Premium Python Portfolio - Abdul Basith H

A high-end, dark-themed portfolio website built with Python (Flask) and Tailwind CSS. Designed to look like a top AI engineer's portfolio from 2026.

## 🚀 Quick Start

1.  **Install Dependencies** (if needed):
    ```bash
    pip install flask
    ```

2.  **Run the Application**:
    ```bash
    python app.py
    ```

3.  **View in Browser**:
    Open `http://127.0.0.1:5000`

## 📁 Project Structure

```
/portfolio
├── app.py              # Flask backend
├── static/
│   ├── css/
│   │   └── style.css   # Custom animations & glassmorphism
│   └── js/
│       └── script.js   # Interactivity & scroll effects
└── templates/
    └── index.html      # Main portfolio page (Tailwind CSS)
```

## 🌐 Deployment Instructions

### Option 1: Render.com (Recommended for Free Hosting)
1.  Create a `requirements.txt` file:
    ```
    Flask==3.0.0
    gunicorn==21.2.0
    ```
2.  Push your code to GitHub.
3.  Sign up on [Render.com](https://render.com).
4.  Click **New +** -> **Web Service**.
5.  Connect your GitHub repository.
6.  Use the following settings:
    - **Runtime**: Python 3
    - **Build Command**: `pip install -r requirements.txt`
    - **Start Command**: `gunicorn app:app`
7.  Click **Create Web Service**.

### Option 2: PythonAnywhere
1.  Sign up for a free account on [PythonAnywhere](https://www.pythonanywhere.com/).
2.  Go to the **Web** tab and add a new web app.
3.  Select **Flask** and the correct Python version.
4.  Upload your files using the **Files** tab.
5.  Reload the web app.

## ✨ Features
- **Dark Luxury Theme**: Deep navy background with electric blue accents.
- **Glassmorphism**: Modern frosted glass effects on cards.
- **Responsive**: Fully optimized for mobile and desktop.
- **Animations**: Scroll-based fade-ins using Intersection Observer.
- **Clean Code**: SEO-friendly HTML and organized CSS/JS.
