# 🔐 Password Strength Checker

## 📝 Description

This project is a simple yet effective **Password Strength Checker** built with Python. It evaluates the strength of a given password based on key characteristics like length, character diversity (uppercase, lowercase, numbers, and special characters), and provides real-time **feedback** and a **score** out of 5. It runs in the command line and is ideal for educational purposes, personal use, or integration into other tools that require password validation.

---

## ⚙️ Features

- ✅ Scores passwords on a scale of **0–5**
- 📊 Classifies passwords as **Weak**, **Moderate**, or **Strong**
- 🧠 Provides **customized feedback** to help users improve their passwords
- 🧪 Uses **regular expressions** for accurate character pattern matching
- 💡 Lightweight and beginner-friendly

---

## 🚀 Getting Started

### ✅ Requirements

- Python 3.x (no external libraries needed)

### ▶️ Running the Script

You can run it from the command line:

```bash
python password_checker.py
```

### 🖥️ Sample Output

```
Password Strength Checker
Enter a password to evaluate: P@ss12

Score: 4 / 5
Strength: Moderate

Suggestions to improve your password:
 - Make your password at least 8 characters long.
```

---

## 🔍 Evaluation Criteria

| Criterion            | Requirement                                  | Points |
|---------------------|----------------------------------------------|--------|
| Length              | At least 8 characters                        | +1     |
| Lowercase Letter    | At least one lowercase letter                | +1     |
| Uppercase Letter    | At least one uppercase letter                | +1     |
| Number              | At least one digit                           | +1     |
| Special Character   | At least one special character (`!@#$...`)   | +1     |

---

## 📂 File Structure

```
password_checker.py       # Main script for evaluating password strength
```

---

## 📌 Notes

- Passwords scoring **5/5** are considered **Strong**.
- Scores **3–4** are **Moderate**, and anything **2 or less** is **Weak**.
- The special characters set can be customized via the `SPECIAL_CHARACTERS` constant.

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

---

Let me know if you’d like to add:
- A **GUI version** (using Tkinter or PyQt)
- **Real-time feedback** while typing (interactive mode)
- Integration with **password breach APIs** like `HaveIBeenPwned`

I'm happy to help extend the functionality!
