# BULLS AND COWS - Flask Web Application

A Flask-based web application for the number-guessing game **Bulls and Cows**. The game generates a secret number based on user input, and the player attempts to guess it. Feedback is provided for each guess with the number of **bulls** (correct digits in the wrong position) and **cows** (correct digits in the correct position).

---

## Features

### Secret Number Generation
- Generates a random secret number with a user-specified number of digits.
- Ensures all digits are unique and the first digit is not zero.
- Stores the secret number in a file (`secretcode.txt`).

### Guess Validation
- Checks that guesses are valid numbers with the correct number of digits.
- Calculates bulls and cows for each guess.

### Session Management
- Stores the secret number, guesses, and other game data using Flask sessions.
- Supports resetting the game to start over.

### User Interface
- Web interface to:
  - Set the number of digits for the secret number.
  - Enter guesses and receive feedback.
- Displays guesses, errors, and success messages dynamically.

---

## How to Run the Application

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/bulls-and-cows.git
   cd bulls-and-cows
   ```
2.**Install Dependencies**
   ```bash
     pip install flask
```
3. **Run Application**
   ```bash
   python app.py
   ```
4. **Acess the Application**
   ```arduino
   http://127.0.0.1:5000/
   ```


### Example Gameplay
- Player sets the number of digits to 4.
- Secret number is generated: 1234 (hidden).
**Player guesses**:
- Guess: 4321 → 2 Bulls, 2 Cows
- Guess: 1234 → 4 Bulls, 0 Cows
- Success message: "Congratulations! You guessed the secret number!"

### File Structure
```csharp
bulls-and-cows/
├── app.py             # Main Flask application
├── templates/
│   ├── index.html     # Homepage template
│   ├── game.html      # Game page template
├── secretcode.txt     # Secret number storage
└── README.md          # Documentation
```

### Game Rules
- Specify the number of digits for the secret number.
- Guess the number, and the app provides feedback:
- Bulls: Correct digits in the wrong position.
- Cows: Correct digits in the correct position.
- Continue guessing until you guess the secret number correctly.

