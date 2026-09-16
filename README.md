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
| 06 | Strings — indexing, slicing, encoding | ✅ Done |
| 07 | Lists | ✅ Done |
| 08 | Tuples & membership testing | ✅ Done |
| 09 | Operator overloading & `bytearray` | ✅ Done |
| 10 | Sets & `frozenset` | ✅ Done |
| 11 | Dictionaries | ✅ Done |
| 12 | `collections` module (intro) | ✅ Done |
| 13 | Conditionals & loops | 🔜 Next |

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
| `frozenset` | `bytearray` |
| `bytes` | |

---

### 6. Strings — Indexing, Slicing & Encoding

**Indexing** pulls out one character. Counting starts at `0`, and negative indexes count backwards from the end.

```python
text = "Python"

text[0]     # 'P'   — first
text[5]     # 'n'   — last
text[-1]    # 'n'   — last, the readable way
text[-6]    # 'P'
text[10]    # ❌ IndexError: string index out of range
```

**Slicing** pulls out a range — `[start : stop : step]`. `start` is included, `stop` is not.

```python
text = "Python"

text[0:3]     # 'Pyt'    — index 0, 1, 2
text[:3]      # 'Pyt'    — start defaults to 0
text[2:]      # 'thon'   — stop defaults to the end
text[:]       # 'Python' — full copy
text[::2]     # 'Pto'    — every 2nd character
text[::-1]    # 'nohtyP' — reversed
```

Unlike indexing, **slicing never throws** — an out-of-range slice just returns what it can:

```python
text[2:100]   # 'thon'  — no error
```

Strings are immutable, so you can read a character but not overwrite one:

```python
text[0] = "J"           # ❌ TypeError
text = "J" + text[1:]   # ✅ build a new string instead
```

**Encoding** is how text becomes bytes. Python strings are Unicode; files, sockets and APIs move raw bytes. `encode()` goes one way, `decode()` goes back.

```python
s = "chai ☕"

b = s.encode("utf-8")     # b'chai \xe2\x98\x95'  → bytes
print(type(b))            # <class 'bytes'>
print(len(s))             # 6  — characters
print(len(b))             # 8  — bytes (the ☕ takes 3)

back = b.decode("utf-8")  # 'chai ☕'
```

UTF-8 is the default and what you should use unless you have a specific reason not to. Decoding bytes with the wrong codec is where `UnicodeDecodeError` and mojibake come from.

---

### 7. Lists

An ordered, **mutable** collection. Can hold mixed types, allows duplicates.

```python
items = [1, "two", 3.0, True, [5, 6]]

items[0]        # 1
items[-1]       # [5, 6]
items[1:3]      # ['two', 3.0]  — slicing works like strings
len(items)      # 5
```

**Mutating in place:**

```python
nums = [3, 1, 2]

nums.append(4)        # [3, 1, 2, 4]        — add one to the end
nums.insert(0, 0)     # [0, 3, 1, 2, 4]     — add at an index
nums.extend([5, 6])   # [0, 3, 1, 2, 4, 5, 6] — add many
nums.remove(3)        # removes the first 3 by value
nums.pop()            # removes & returns the last item
nums.pop(0)           # removes & returns by index
nums.sort()           # sorts in place, returns None
nums.reverse()        # reverses in place
nums.clear()          # empties it
```

> ⚠️ `sort()` mutates and returns `None`. `sorted(nums)` returns a **new** sorted list and leaves the original alone. Assigning `nums = nums.sort()` sets `nums` to `None` — a classic beginner bug.

**Copying:** a list variable is a reference, not the data.

```python
a = [1, 2, 3]
b = a           # same object — both names point to one list
b.append(4)
print(a)        # [1, 2, 3, 4]  ← a changed too

c = a.copy()    # or a[:] or list(a) — a real (shallow) copy
```

---

### 8. Tuples & Membership Testing

A tuple is an ordered collection like a list, but **immutable**.

```python
point = (10, 20)
single = (42,)        # the trailing comma is what makes it a tuple
not_a_tuple = (42)    # this is just an int

point[0]              # 10
point[0] = 99         # ❌ TypeError — cannot be changed
```

Only two methods, because there's nothing to mutate: `.count()` and `.index()`.

**Unpacking:**

```python
x, y = point                    # x = 10, y = 20
a, *rest = (1, 2, 3, 4)         # a = 1, rest = [2, 3, 4]
```

**Why use a tuple over a list?**

- Signals "this shouldn't change" — fixed records, coordinates, config
- Hashable, so it can be a dict key or set member
- Slightly faster and lighter than a list

```python
locations = {(28.61, 77.20): "Delhi"}    # ✅ tuple key works
locations = {[28.61, 77.20]: "Delhi"}    # ❌ TypeError: unhashable type: 'list'
```

**Membership testing** — `in` and `not in` work on every sequence:

```python
3 in [1, 2, 3]              # True
"y" in "Python"             # True
"key" in {"key": "value"}   # True  — checks KEYS, not values
5 not in (1, 2, 3)          # True
```

Speed matters here. `in` on a list or tuple scans item by item — **O(n)**. On a set or dict it's a hash lookup — **O(1)**. For big collections of lookups, use a set.

---

### 9. Operator Overloading & `bytearray`

**Operator overloading** means the same operator does different things depending on the type. Python maps operators to dunder (double underscore) methods.

```python
2 + 3              # 5           — int.__add__
"chai" + " code"   # 'chai code' — str.__add__ concatenates
[1, 2] + [3]       # [1, 2, 3]   — list.__add__ joins

3 * 2              # 6
"ab" * 3           # 'ababab'
[0] * 3            # [0, 0, 0]
```

Common dunders behind the scenes:

| Operator | Method |
|----------|--------|
| `+` | `__add__` |
| `-` | `__sub__` |
| `*` | `__mul__` |
| `==` | `__eq__` |
| `<` | `__lt__` |
| `len(x)` | `__len__` |
| `x[i]` | `__getitem__` |
| `in` | `__contains__` |
| `str(x)` | `__str__` |

You can define them on your own classes:

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"₹{self.amount}"

print(Money(100) + Money(50))    # ₹150
```

**`bytes` vs `bytearray`** — both hold raw bytes. `bytes` is immutable, `bytearray` is the mutable version.

```python
b = bytes([72, 101, 108, 108, 111])   # b'Hello' — immutable
b[0] = 74                              # ❌ TypeError

ba = bytearray(b"Hello")               # mutable
ba[0] = 74
print(ba)                              # bytearray(b'Jello')

ba.append(33)                          # bytearray(b'Jello!')
ba.decode("utf-8")                     # 'Jello!'
```

Use `bytearray` when you're building up or patching binary data — file chunks, network buffers, image bytes — without creating a new object on every change.

---

### 10. Sets & `frozenset`

A set is an **unordered** collection of **unique**, hashable items. No indexing, no duplicates.

```python
s = {3, 1, 2, 2, 3}
print(s)            # {1, 2, 3} — duplicates dropped

empty = set()       # {} creates an empty DICT, not a set
s[0]                # ❌ TypeError — not subscriptable
```

**Methods:**

```python
s.add(4)            # add one
s.update([5, 6])    # add many
s.discard(10)       # remove if present — no error if missing
s.remove(10)        # ❌ KeyError if missing
s.pop()             # removes an arbitrary item
```

**Set operations** — the reason sets exist:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b    # {1, 2, 3, 4, 5, 6}  union
a & b    # {3, 4}              intersection
a - b    # {1, 2}              difference
a ^ b    # {1, 2, 5, 6}        symmetric difference
```

Everyday use: dropping duplicates and fast membership tests.

```python
unique = list(set([1, 1, 2, 3, 3]))    # [1, 2, 3] — order not guaranteed
```

**`frozenset`** is the immutable set. Since it can't change, it's hashable — so it can go inside another set or be a dict key.

```python
fs = frozenset([1, 2, 3])
fs.add(4)                 # ❌ AttributeError

nested = {frozenset([1, 2]), frozenset([3, 4])}    # ✅ set of sets
```

---

### 11. Dictionaries

Key–value pairs. Mutable, and since Python 3.7 they keep **insertion order**. Keys must be hashable (so immutable); values can be anything.

```python
user = {"name": "Abhinav", "city": "Delhi", "active": True}

user["name"]              # 'Abhinav'
user["age"]               # ❌ KeyError
user.get("age")           # None      — safe
user.get("age", 0)        # 0         — with a default
```

**Modifying:**

```python
user["age"] = 25                      # add or overwrite
user.update({"city": "Noida"})        # merge in another dict
user.pop("active")                    # remove & return the value
del user["city"]                      # remove
user.setdefault("role", "engineer")   # set only if the key is missing
```

**Iterating:**

```python
for key in user:                      # keys by default
    print(key)

for key, value in user.items():       # the useful one
    print(key, "→", value)

user.keys()      # dict_keys([...])
user.values()    # dict_values([...])
user.items()     # dict_items([(k, v), ...])
```

**Comprehensions** work here too:

```python
squares = {n: n**2 for n in range(5)}       # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

**Nesting** is how JSON-shaped data gets modelled:

```python
data = {
    "user": {"name": "Abhinav", "langs": ["JS", "Python"]}
}
data["user"]["langs"][1]      # 'Python'
```

---

### 12. Advanced Data Types — `collections`

The standard library ships specialised containers built on top of the basics. A quick tour:

**`Counter`** — counts things.

```python
from collections import Counter

c = Counter("mississippi")
print(c)                  # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
print(c.most_common(2))   # [('i', 4), ('s', 4)]
```

**`defaultdict`** — a dict that creates missing values instead of raising `KeyError`.

```python
from collections import defaultdict

groups = defaultdict(list)
groups["fruits"].append("mango")     # no need to initialise the list first
print(groups)                        # defaultdict(<class 'list'>, {'fruits': ['mango']})
```

**`namedtuple`** — a tuple with named fields, so you stop writing `point[0]`.

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)      # 10 20
```

**`deque`** — a double-ended queue. `O(1)` appends and pops at *both* ends, where a list is `O(n)` at the front.

```python
from collections import deque

d = deque([1, 2, 3])
d.appendleft(0)      # deque([0, 1, 2, 3])
d.popleft()          # 0
```

**`OrderedDict`** — order-preserving dict. Mostly historical now that regular dicts keep order, but it has order-aware equality and `move_to_end()`.

| Container | Reach for it when |
|-----------|-------------------|
| `Counter` | Counting frequencies |
| `defaultdict` | Grouping / accumulating |
| `namedtuple` | Lightweight records |
| `deque` | Queues, stacks, sliding windows |
| `OrderedDict` | Order-sensitive comparisons |

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
├── 03_strings/
│   ├── indexing_slicing.py
│   └── encoding_decoding.py
├── 04_lists/
├── 05_tuples/
│   └── membership_testing.py
├── 06_operator_overloading/
│   └── bytearray_demo.py
├── 07_sets/
│   └── frozenset.py
├── 08_dictionaries/
├── 09_collections/
│   ├── counter.py
│   ├── defaultdict.py
│   ├── namedtuple.py
│   └── deque.py
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
- [x] Strings — indexing, slicing, encoding
- [x] Lists, tuples, sets, dictionaries
- [x] Operator overloading & `bytearray`
- [x] `collections` module (intro)
- [ ] Operators & conditionals
- [ ] Loops
- [ ] Functions
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