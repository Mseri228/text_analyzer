# Text Analyzer

A Flask web app that analyzes text and manages a list of students.

## Features
- Text analyzer at `/post`: character count, word count, top 10 words
- Students page at `/students`
- Join form at `/join` to add a student
- JSON API at `/api/v1.0/students` (GET and POST)

## Run it
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
Then open http://127.0.0.1:5001