from flask import Flask, render_template, request
from random import choice
from replit import db

app = Flask(__name__)

if 'guesses' not in db:
  db['guesses'] = []

if 'answer' not in db:
  db['answer'] =  choice(range(1,101))
  


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    guess = int(request.form['number_guess'])
    message = check_number_show_message(guess, db['answer'])
    db['guesses'].append(message)
    print(message)
    
  return render_template('index.html', guesses=reversed(db['guesses']))

@app.route('/reset')
def reset():
  db['answer'] = choice(range(1,101))
  db['guesses'] = []
  return render_template('index.html', guesses=db['guesses'])

def check_number_show_message(guess, answer):
  if guess > answer:
    return f'{guess} is Too high'
  elif guess < answer:
    return f'{guess} is Too low'
  else:
    return 'You got it!'
    
app.run(host='0.0.0.0', port=81)