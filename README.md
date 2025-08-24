# Portofolio Website

A personal portfolio website built with Python Flask that showcases GitHub projects.

## Features

- Responsive design
- Project showcase with filtering
- About section with skills
- Contact form
- Integration with GitHub API

---

## Repo Structure
```
portofolio-website/
├── app.py
├── requirements.txt
├── .gitignore
├── config.py
├── README.md
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       ├── ..
└── templates/
    ├── base.html
    ├── index.html
    ├── projects.html
    ├── about.html
    └── contact.html
```

---

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Set up environment variables (optional):
   - Create a `.env` file
   - Add `SECRET_KEY=your-secret-key`
6. Run the application: `python app.py`
7. Open your browser and go to `http://localhost:5000`

---

## Customization

1. Replace `your-github-username` in `app.py` with your actual GitHub username
2. Update personal information in the templates
3. Add your own images to the `static/images` folder
4. Customize the styling in `static/css/style.css`

---

## Deployment

The application can be deployed to platforms like:
- Heroku
- PythonAnywhere
- Vercel (with serverless functions)
- AWS Elastic Beanstalk

---

## License

This project is open source and available under the [MIT License](LICENSE).