# 🐍 Python + AI — Learning from Scratch

A daily log of my journey learning Python and AI fundamentals, following **Hitesh Choudhary's** course.
Every concept I learn gets written as code and pushed here the same day — no skipped days, no copy-paste without understanding.

---

## 📌 About This Repo

This is a learning repository, not a polished project. Expect:

- Small, focused scripts — one concept per file
- Comments explaining *why*, not just *what*
- Mistakes left in place (with fixes below them) so I can look back later
- Daily commits, even if it's 10 lines

If you're learning Python too, feel free to browse. If you spot something wrong, open an issue — I'd rather be corrected than confidently wrong.

---

## ✅ Progress So Far

| # | Topic | Status |
|---|-------|--------|
| 01 | What Python is & where it's actually used | ✅ Done |
| 02 | Installing Python & setting up the environment | ✅ Done |
| 03 | Virtual environments (`.venv`) | ✅ Done |
| 04 | Python syntax basics | ✅ Done |
| 05 | Variables & data types | 🔜 Next |

---

## 📚 Notes

### 1. Where Python Is Used

Python is a general-purpose language, which is why it shows up almost everywhere:

- **AI / Machine Learning** — PyTorch, TensorFlow, scikit-learn
- **Data Science & Analysis** — pandas, NumPy, Matplotlib
- **Backend / APIs** — Django, Flask, FastAPI
- **Automation & Scripting** — file handling, scraping, repetitive task automation
- **DevOps tooling** — deployment scripts, infra automation
- **Testing** — pytest, Selenium

The reason it dominates AI specifically: readable syntax, a massive library ecosystem, and heavy C/C++ under the hood doing the fast math while you write simple Python on top.

---

### 2. Virtual Environments (`.venv`)

A virtual environment is an isolated Python setup **per project**. Without it, every package you install goes global, and two projects needing different versions of the same library will break each other.

**Create one:**

```bash
python -m venv .venv
```

**Activate it:**

```bash
# macOS / Linux
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (CMD)
.venv\Scripts\activate.bat
```

You'll know it worked when your terminal prompt shows `(.venv)` at the start.

**Install packages & save them:**

```bash
pip install <package-name>
pip freeze > requirements.txt
```

**Restore on another machine:**

```bash
pip install -r requirements.txt
```

**Deactivate:**

```bash
deactivate
```

> ⚠️ Always add `.venv/` to `.gitignore`. It's machine-specific and can be hundreds of MB. Commit `requirements.txt` instead — that's the actual source of truth.

---

### 3. Python Syntax Basics

Things that stood out coming into Python:

**Indentation is the syntax.** No curly braces. Whitespace defines blocks, and getting it wrong is an actual error, not a style complaint.

```python
if temperature > 30:
    print("It's hot")     # inside the if
print("Done")             # outside the if
```

**No semicolons, no type declarations.**

```python
name = "Abhinav"      # str
age = 25              # int
height = 5.9          # float
is_learning = True    # bool
```

**Comments:**

```python
# single line comment

"""
multi-line string, commonly
used as a docstring
"""
```

**Printing & input:**

```python
print("Hello, World!")
print(f"My name is {name} and I am {age}")   # f-string

user_name = input("Enter your name: ")        # always returns a string
user_age = int(input("Enter your age: "))     # cast when you need a number
```

**Running a file:**

```bash
python filename.py
```

---

## 🗂️ Folder Structure

```
.
├── 01_basics/
│   ├── hello_world.py
│   ├── variables.py
│   └── syntax_practice.py
├── 02_.../
├── requirements.txt
├── .gitignore
└── README.md
```

Each folder maps to a topic. Files inside are numbered in the order I learned them.

---

## 🚀 Running the Code

```bash
git clone <your-repo-url>
cd <repo-name>

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt
python 01_basics/hello_world.py
```

---

## 🎯 Roadmap

- [x] Python use cases & setup
- [x] Virtual environments
- [x] Basic syntax
- [ ] Variables, data types, type casting
- [ ] Operators & conditionals
- [ ] Loops
- [ ] Functions
- [ ] Lists, tuples, sets, dictionaries
- [ ] Strings in depth
- [ ] File handling
- [ ] Error handling
- [ ] OOP in Python
- [ ] Modules & packages
- [ ] NumPy & pandas
- [ ] Math for AI (vectors, matrices, basic stats)
- [ ] Machine learning fundamentals
- [ ] Neural networks & deep learning
- [ ] Building projects

---

## 🙏 Credits

Learning from **[Hitesh Choudhary](https://www.youtube.com/@chaiaurcode)** — Chai aur Code.

---

⭐ Consistency over intensity. See you in tomorrow's commit.
