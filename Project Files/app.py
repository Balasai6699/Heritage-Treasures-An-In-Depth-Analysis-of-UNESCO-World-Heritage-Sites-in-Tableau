from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    """Dashboard page with embedded Tableau visualizations"""
    return render_template('dashboard.html')

@app.route('/story')
def story():
    """Story page with embedded Tableau story"""
    return render_template('story.html')

@app.route('/about')
def about():
    """About page with project information"""
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
