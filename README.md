# Smart Quiz & Exam System

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)]()
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

> A comprehensive, pure Python console application for managing questions, conducting quizzes, logging results, analyzing statistics, and handling edge cases with zero external database dependencies.

---

## Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Project Architecture](#-project-architecture)
- [Concepts & Technical Requirements](#-concepts--technical-requirements)
- [Challenge Tasks Solved](#-challenge-tasks-solved)
- [Getting Started](#-getting-started)
- [Running Unit Tests](#-running-unit-tests)
- [License](#-license)

---

## 🌟 Overview

The **Smart Quiz & Exam System** is a modular console-based application written entirely in Python. It provides a complete end-to-end solution for:
- User authentication with security attempt limits.
- Interactive question bank CRUD operations.
- Dynamic quiz execution with difficulty filtering and automated grading.
- Persistent file storage (`data/questions.txt` and `data/results.txt`).
- Detailed statistical reporting and automated unit test verification.

Designed strictly using core fundamentals from **Python Crash Course** (variables, control statements, functions, lists, dictionaries, file I/O, exception handling, and standard `unittest`).

---

## Key Features

1. ** Secure User Authentication (`Authentication.py`):**
   - Username and password verification.
   - Enforces a maximum of **3 login attempts**. Exits cleanly if authentication fails.

2. ** Interactive Main Menu (`main.py`):**
   ```text
   ======================== SMART QUIZ SYSTEM ========================
    1. Start Quiz
    2. View Previous Results
    3. Add Question
    4. Delete Question
    5. Search Question
    6. Statistics
    7. Exit
   ==================================================================
   ```

3. ** Question Bank Management (`questions.py`):**
   - **Add Question:** Input Question ID, question text, 4 options (A, B, C, D), correct answer, and difficulty (`Easy`, `Medium`, `Hard`).
   - **Delete Question:** Delete by unique Question ID with confirmation prompt.
   - **Search Question:** Search by Question ID, keyword in text, or difficulty level.

4. ** Quiz Engine & Scoring (`quiz.py`):**
   - Filter questions by difficulty or attempt all available questions.
   - Case-insensitive (`a` vs `A`) and space-tolerant (` A `) answer evaluation.
   - Calculates total score, wrong answers, percentage, and status (`PASSED` if score ≥ 50%, else `FAILED`).

5. ** Results Logging & Viewing (`result.py`):**
   - Automatically appends attempt timestamps, username, score, percentage, and status to `data/results.txt`.
   - Displays a formatted tabular history of past quiz attempts.

6. **📊 System Analytics (`statistics.py`):**
   - Summarizes total questions and breakdown by difficulty (`Easy`, `Medium`, `Hard`).
   - Computes historical metrics: total attempts, highest score, average percentage, and pass rate.

---

##  Project Architecture

```text
project/
│
├── main.py              # Application entry point & menu control loop
├── Authentication.py    # Login authentication & attempt limiter
├── questions.py         # Question CRUD, file storage & searching
├── quiz.py              # Quiz execution engine, answer evaluation & scoring
├── result.py            # Results persistence and formatted history viewer
├── statistics.py        # System metrics & score analytics
├── test_quiz.py         # Unit tests suite using Python's unittest library
│
└── data/
    ├── questions.txt    # Persistent JSON Lines question bank
    └── results.txt      # Persistent JSON Lines quiz attempt history
```

---

##  Concepts & Technical Requirements

| Python Concept | Implementation in Project |
| :--- | :--- |
| **Data Types** | `int`, `float`, `str`, `bool` used for IDs, scores, texts, and flags. |
| **Data Structures** | `list` for option lists and questions; `dict` for structured question data (`id`, `question`, `options`, `answer`, `difficulty`). |
| **Control Flow** | `if-elif-else` for menu choices, authentication, and grading logic. |
| **Loops** | `while` loops for continuous menus/inputs; `for` loops for questions display and searching. |
| **Functions** | Modular function structure (`login()`, `start_quiz()`, `add_question()`, `check_answer()`, `calculate_score()`). |
| **File Handling** | Safe reading and writing with `with open(filepath, ...)` utilizing JSON serialization. |
| **Exception Handling** | `try-except` blocks handling `ValueError`, `FileNotFoundError`, and `json.JSONDecodeError`. |
| **Unit Testing** | Test coverage using standard `unittest.TestCase`. |

---

##  Challenge Tasks Solved

| # | Challenge Requirement | Implementation Detail |
|---|-----------------------|-----------------------|
| **1** | **Invalid Question Count Handling** | Automatically caps and prompts if requested question count exceeds available questions. |
| **2** | **Case-Insensitive Answers** | Standardizes user input using `.strip().upper()` so `"a"` and `"A"` evaluate identically. |
| **3** | **Whitespace Tolerant Input** | Trims leading/trailing spaces (`" A "` → `"A"`). |
| **4** | **Empty Input Prevention** | Validates user inputs in a `while` loop until non-empty values are provided. |
| **5** | **Duplicate Question ID Check** | Checks existing question IDs before insertion to guarantee uniqueness. |
| **6** | **Graceful First-Run File Handling** | Automatically creates default questions and empty results files if missing on initial run. |
| **7** | **Zero-Crash Resilience** | Wraps user inputs and main execution loop in `try-except` blocks to prevent unexpected crashes. |

---

##  Getting Started

### Prerequisites

- **Python 3.8+** installed on your system.

### Running the Application

1. Clone or download this repository.
2. Open a terminal in the project directory:
   ```bash
   cd project
   ```
3. Run the main script:
   ```bash
   python main.py
   ```

### Default Login Credentials

- **Username:** `admin`
- **Password:** `admin123`

---

##  Running Unit Tests

The test suite covers login validation, answer evaluation (case & space sensitivity), score calculation, and search logic.

Run the tests using Python's built-in `unittest` runner:

```bash
python test_quiz.py
```

or:

```bash
python -m unittest test_quiz.py
```

### Expected Output:

```text
............
----------------------------------------------------------------------
Ran 12 tests in 0.001s

OK
```

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
