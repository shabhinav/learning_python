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
| 05 | Numbers — `int`, `float`, `bool` | ✅ Done |
| 06 | Strings | 🔜 Next |

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

### 4. Numbers

Python has three number types you use day to day:

| Type | What it holds | Example |
|------|---------------|---------|
| `int` | Whole numbers, positive or negative | `42`, `-7`, `0` |
| `float` | Real numbers (decimals) | `3.14`, `-0.5`, `2.0` |
| `bool` | Truth values | `True`, `False` |

```python
count = 42          # int
price = 99.99       # float
is_active = True    # bool

print(type(count))      # <class 'int'>
print(type(price))      # <class 'float'>
print(type(is_active))  # <class 'bool'>
```

**`int` has no size limit.** Unlike most languages, Python integers grow as large as your memory allows — no overflow to worry about.

```python
big = 2 ** 200
print(big)   # prints the whole thing, no wraparound
```

**`bool` is actually a subclass of `int`.** `True` is `1` and `False` is `0` under the hood, which is why this works:

```python
print(True + True)    # 2
print(False * 10)     # 0
print(isinstance(True, int))   # True
```

**Type casting between them:**

```python
int("25")      # 25    — string to int
float(7)       # 7.0   — int to float
int(9.99)      # 9     — truncates, does NOT round
bool(0)        # False — 0 is falsy, every other number is truthy
```

---

### 5. Numbers Are Immutable

This is the part that clicked for me today.

**A number object can never be changed.** When you "update" a number, Python doesn't edit the existing object — it creates a new one and points the variable name at it.

```python
x = 10
print(id(x))    # e.g. 140712834567890

x = x + 1
print(id(x))    # DIFFERENT id — this is a brand new object
```

The name `x` moved. The original `10` was never touched.

**Compare that with a set, which is mutable:**

```python
numbers = {1, 2, 3}
print(id(numbers))    # e.g. 140712834111000

numbers.add(4)
print(id(numbers))    # SAME id — the object itself changed in place
print(numbers)        # {1, 2, 3, 4}
```

The set was modified in place. Same object, new contents.

**Why it matters:**

- Immutable objects are safe to share — nothing can change them behind your back
- They can be used as dictionary keys and set members (mutable objects can't)
- Every arithmetic operation produces a *new* object, it never mutates the old one

```python
# immutable → can be a dict key
scores = {1: "first", 2: "second"}     # ✅ works

# mutable → cannot be a dict key
broken = {{1, 2}: "value"}             # ❌ TypeError: unhashable type: 'set'
```

**Quick reference:**

| Immutable | Mutable |
|-----------|---------|
| `int`, `float`, `bool` | `list` |
| `str` | `set` |
| `tuple` | `dict` |

---

## 🗂️ Folder Structure

```
.
├── 01_basics/
│   ├── hello_world.py
│   ├── variables.py
│   └── syntax_practice.py
├── 02_numbers/
│   ├── int_float_bool.py
│   ├── type_casting.py
│   └── immutability.py
├── 03_.../
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
- [x] Variables & type casting
- [x] Numbers — `int`, `float`, `bool`, immutability
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