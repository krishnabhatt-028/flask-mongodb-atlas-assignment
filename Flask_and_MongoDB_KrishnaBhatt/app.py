import json
import os
from pathlib import Path
from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "change-this-secret-key")
MONGO_URI = os.getenv("MONGO_URI", "")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "flask_assignment")
MONGO_COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME", "submissions")

def get_collection():
    if not MONGO_URI:
        raise RuntimeError("MONGO_URI is not configured. Add it to your .env file.")
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.admin.command("ping")
    return client[MONGO_DB_NAME][MONGO_COLLECTION_NAME]

def load_api_data():
    with (BASE_DIR / "backend" / "data.json").open("r", encoding="utf-8") as file:
        return json.load(file)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/api")
def api_data():
    try:
        return jsonify(load_api_data())
    except (OSError, json.JSONDecodeError) as exc:
        return jsonify({"error": f"Could not read backend data: {exc}"}), 500

@app.post("/submit")
def submit_form():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()
    form_data = {"name": name, "email": email, "message": message}
    if not name or not email or not message:
        return render_template("index.html", error="Please fill in all fields before submitting.", form_data=form_data), 400
    try:
        get_collection().insert_one(form_data)
        return redirect(url_for("success"))
    except (PyMongoError, RuntimeError) as exc:
        return render_template("index.html", error=f"Unable to save data: {exc}", form_data=form_data), 500

@app.get("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
