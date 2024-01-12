import os
from flask import Flask, render_template
from werkzeug.utils import quote
import importlib.metadata
import random

app = Flask(__name__)

# Зчитайте список ігор з текстового файлу
with open('games_list.txt', 'r', encoding='utf-8') as file:
    games = [line.strip() for line in file]

@app.route('/')
def index():
    return render_template('index.html', games=games, version=importlib.metadata.version("flask"))

@app.route('/spin')
def spin_wheel():
    # Виберіть випадкову гру
    selected_game = random.choice(games)
    return render_template('result.html', selected_game=selected_game)

if __name__ == '__main__':
# Використовуйте PORT, який задається Heroku
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)