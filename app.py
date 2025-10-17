# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for feedback
feedback_store = []

@app.route('/')
def home():
    return "Welcome to the Teacher Feedback App!"
