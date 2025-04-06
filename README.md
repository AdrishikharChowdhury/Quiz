
# 🧠 Terminal Quiz Game (Python CLI)

Welcome to a fun and interactive **Quiz Game** built using Python! This is a simple, console-based trivia application where users can test their general knowledge. Whether you're a beginner learning Python or just want to challenge yourself with random facts, this quiz game has you covered.

---

## 📌 Overview

This Python program quizzes the user with a set of multiple-choice questions on general knowledge. It includes features like:

- Score tracking
- Real-time answer validation
- Case-insensitive answer checking
- Modular code design

Everything runs in the terminal, with a clean and intuitive flow.

---

## 🧩 Features

- 🧠 10 general knowledge questions
- ✅ Instant answer verification
- 🎯 Score tracking with user name
- 🚫 Warns about case sensitivity and spelling
- 🔁 Easy to expand and maintain using modular design

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/python-quiz-game.git
cd python-quiz-game
```

### 2. Run the Game

Make sure you have **Python 3.6+** installed. Then run:

```bash
python main.py
```

---

## 🏗️ Project Structure

```bash
.
├── main.py            # Entry point of the quiz
├── quiz_logic.py      # Core quiz logic (flow, validation)
├── questions.py       # Contains the questions, options, and answers
└── README.md          # Project documentation
```

---

## 📖 How to Play

1. Launch the game using the command line.
2. Enter your name when prompted.
3. Answer each question by typing the correct option (not the number, but the actual answer).
4. Double-check spelling and case – the system matches exact text (but ignores case).
5. After all 10 questions, your final score will be displayed.

---

## 🎮 Sample Gameplay

```text
<===Welcome to the Quiz===>

Disclaimer:
Double check the spelling of the answer before you enter

Enter your name player: John
Score of John is 0

1. What is the capital city of Australia?
    1) Sydney
    2) Melbourne
    3) Canberra
    4) Brisbane
Write your answer: Canberra

...

Congratulations!!
Score of John is 8
```

---

## 🔍 Code Logic

### `main.py`
- Prompts user for name and starts the quiz.
- Displays initial and final score.

### `questions.py`
- Holds the quiz data:
  - `questions`: List of question strings.
  - `options`: List of options (multiple choices).
  - `answers`: Correct answer strings.

### `quiz_logic.py`
- Controls question flow, displays options, and verifies user answers.
- `verify()`: Compares user input against correct answers (case-insensitive).
- `quiz()`: Iterates through questions and updates the score.

---

## 🛠️ Technologies Used

- Python 3
- Standard Library (No external packages)
- Terminal/Command-Line Interface

---

## ✨ Future Improvements

- Support answer selection via number (e.g., enter "2" instead of full answer)
- Add difficulty levels (Easy, Medium, Hard)
- Randomize question order
- Timer-based questions
- Track high scores
- Export results to file (CSV/JSON)
- GUI using `tkinter` or `PyQt`

---

## 💡 Tips

- The quiz currently matches answers based on text comparison.
- Make sure to type answers exactly as they appear in the options.
- Answers are case-insensitive but must match the correct spelling.

---

## 📜 License

This project is open-source and free to use. No license restrictions apply (MIT recommended if you'd like to add one).

---

## 👨‍💻 Author

**[Adrishikhar Chowhdury]**  
Python Developer & Tech Enthusiast  
📧 amiadrishikhar@gmail.com 
🌐 [portfolio](adrishikharchowdhury.glitch.me)

If you find this useful or fun, feel free to give it a ⭐ on GitHub!

---

Enjoy the quiz and keep challenging your brain! 🎉
