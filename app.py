from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)
# Vercel will set the SECRET_KEY environment variable. 
# For local development, it falls back to the default value.
app.secret_key = os.environ.get("SECRET_KEY", "dev_secret_key_change_in_production")

@app.route('/')
def home():
    projects = [
        {
            "title": "Toxic Speech Classification",
            "description": "A Deep Learning model to detect and classify toxic speech from textual data using NLP and Python. Achieved 95% accuracy on Kaggle dataset.",
            "technologies": ["Python", "TensorFlow", "NLP", "Flask"],
            "github_link": "https://github.com/abasith8074", # Placeholder
            "image": "https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" # Placeholder tech image
        }
    ]
    
    certifications = [
        {
            "name": "Oracle Cloud Infrastructure Foundations Associate",
            "issuer": "Oracle",
            "link": "#"
        },
        {
            "name": "Getting Started with Artificial Intelligence",
            "issuer": "IBM",
            "link": "#"
        }
    ]

    return render_template('index.html', title="Abdul Basith | Python Full Stack Developer", projects=projects, certifications=certifications)

@app.route('/contact', methods=['POST'])
def contact():
    # In a real production app, you'd send an email here or save to DB
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # Simulate processing
    # print(f"Message from {name} ({email}): {message}")
    
    flash("Message sent successfully! I'll get back to you soon.", "success")
    return redirect(url_for('home', _anchor='contact'))

if __name__ == '__main__':
    app.run(debug=True)
