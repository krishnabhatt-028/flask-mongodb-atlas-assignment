# flask-mongodb-atlas-assignment
Flask web application with MongoDB Atlas integration, JSON API, frontend form, and success/error handling.
# Flask & MongoDB Atlas

A Flask web application that provides a JSON API and stores form data in **MongoDB Atlas**.

## Features

* Flask `/api` JSON API
* Reads API data from a JSON file
* Frontend form
* MongoDB Atlas integration
* Success and error handling

## Tech Stack

* Python
* Flask
* MongoDB Atlas
* PyMongo
* HTML/CSS

## Project Structure

```text
Flask_and_MongoDB_KrishnaBhatt/
├── app.py
├── requirements.txt
├── backend/
│   └── data.json
├── templates/
│   ├── index.html
│   └── success.html
└── static/
    └── style.css
```

## Setup

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
cd Flask_and_MongoDB_KrishnaBhatt
pip install -r requirements.txt
```

Create a `.env` file:

```env
MONGO_URI=your_mongodb_atlas_connection_string
```

Run:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## API

```text
GET /api
```

## Author

**Krishna Bhatt**

GitHub: https://github.com/krishnabhatt-028
LinkedIn: https://linkedin.com/in/krishnabhatt0
