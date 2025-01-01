from flask import Flask, render_template, request, session, redirect, url_for
import random
import string

app = Flask(__name__)
app.secret_key = "supersecretkey"

def generate_secret_number(num_digits):
    """Generates a random secret number with the given number of digits, following rules, and stores it in a file."""
    if num_digits<0:
        raise ValueError("Number of digits should be a positive integer.")
    digits = list(string.digits[1:])  # Exclude '0' for the first digit
    first_digit = random.choice(digits)
    remaining_digits = list(string.digits)
    remaining_digits.remove(first_digit)
    secret_number = first_digit + ''.join(random.sample(remaining_digits, num_digits - 1))

    with open("secretcode.txt", "w") as file:
        file.write(secret_number + "\n")
    return secret_number

def check_guess(guess, secret_number):
    """Checks the guess and returns the number of Bulls and Cows."""
    bulls = cows = 0
    for i in range(len(secret_number)):
        if guess[i] == secret_number[i]:
            cows += 1
        elif guess[i] in secret_number:
            bulls += 1
    return bulls, cows

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
      try:
        num_digits = int(request.form['num_digits'])
        if num_digits <=0:
             error = "Please enter a positive number of digits."
             return render_template('index.html', error=error)
        session['num_digits'] = num_digits
        session['secret_number'] = generate_secret_number(num_digits)
        session['guesses'] = []
        return redirect(url_for('game'))
      except ValueError:
            error = "Please enter a valid number."
            return render_template('index.html', error=error)
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if 'secret_number' not in session:
        return redirect(url_for('index'))

    num_digits = session['num_digits']
    secret_number = session['secret_number']
    guesses = session['guesses']

    if request.method == 'POST':
        player_guess = request.form['guess']
        if len(player_guess) != num_digits or not player_guess.isdigit():
            error = f"Please enter a valid {num_digits}-digit number."
            return render_template('game.html', guesses=guesses, error=error)

        bulls, cows = check_guess(player_guess, secret_number)
        guesses.append({'guess': player_guess, 'bulls': bulls, 'cows': cows})
        session['guesses'] = guesses

        if cows == num_digits:
            return render_template('game.html', guesses=guesses, success="Congratulations! You've guessed the secret number.")

    return render_template('game.html', guesses=guesses)

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
