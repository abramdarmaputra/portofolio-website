from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime
import os
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    projects_data = get_github_projects()
    return render_template('projects.html', projects=projects_data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Di sini tambahkan logika pengiriman email
        print(f"Pesan dari {name} ({email}): {message}")
        
        return render_template('contact.html', success=True)
    
    return render_template('contact.html', success=False)

def get_github_projects():
    username = 'abramdarmaputra'  # Ganti dengan username GitHub Anda
    url = f'https://api.github.com/users/abramdarmaputra/repos'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        repos = response.json()
        
        projects = []
        for repo in repos:
            if not repo['fork'] and not repo['is_template']:
                projects.append({
                    'name': repo['name'],
                    'description': repo['description'],
                    'url': repo['html_url'],
                    'language': repo['language'],
                    'stars': repo['stargazers_count'],
                    'forks': repo['forks_count'],
                    'updated_at': format_date(repo['updated_at'])
                })
        
        return sorted(projects, key=lambda x: x['stars'], reverse=True)
    
    except requests.RequestException as e:
        print(f"Error fetching GitHub data: {e}")
        return []

def format_date(date_string):
    try:
        date_obj = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
        return date_obj.strftime('%b %Y')
    except:
        return date_string

if __name__ == '__main__':
    app.run(debug=True)
