from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return 'Data Science CS580N'