Great! Here's a professional and polished `README.md` for your **E-Market Flask Project** based on the repository structure and your previous messages:

---

```markdown
# 🛒 E-Market - Flask Web App

A sleek, responsive, and minimal E-Market application built using **Flask**, **Bootstrap 5**, and **WTForms**. Users can browse available items, purchase them, and manage their owned inventory with dynamic modals and clean UI.

---

## 🔧 Features

- 🔐 User Registration & Login System
- 💼 Market Dashboard
  - View available items
  - Purchase items
  - Sell owned items
- 🧾 Modals for:
  - Item details
  - Purchase confirmation
  - Sell confirmation
- 🪟 Dynamic layout with a toggleable **Owned Items Sidebar**
- 💎 Glassmorphism UI using Bootstrap 5
- 🔍 Search functionality for available items

---

## 📁 Project Structure

```

E-Market/
│
├── Components/
│   ├── **init**.py          # App and DB setup
│   ├── Models.py            # SQLAlchemy models
│   ├── Routes.py            # Flask routes
│   └── Forms.py             # WTForms for login, register, purchase, sell
│
├── Templates/
│   ├── base.html            # Main layout
│   ├── home.html            # Landing page
│   ├── market.html          # Market dashboard
│   ├── Includes/
│   │   ├── items\_modals.html
│   │   └── owned\_items\_modal.html
│
├── static/
│   └── styles.css           # Custom styles
│
├── run.py                   # App entry point
└── README.md                # You’re reading it!

````

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.x
- Flask
- Flask-WTF
- Flask-SQLAlchemy

### 📦 Installation

```bash
# Clone the repo
git clone https://github.com/RealHaroon/Flask-Projects.git
cd Flask-Projects/E-Market

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
````

### 🏃‍♂️ Run the App

```bash
python run.py
```

Visit: `http://127.0.0.1:5000`

---



---

## 🧠 Concepts Used

* Flask Blueprint Architecture
* Jinja2 Templating
* Flask-WTF & CSRF protection
* Bootstrap 5 & Glassmorphism UI
* SQLAlchemy ORM
* Modal UI with Bootstrap

---

## ✍️ Author

**Haroon Khan**
[GitHub @RealHaroon](https://github.com/RealHaroon)

---

## 📜 License

This project is open-source under the MIT License. Feel free to use and modify it.

```

---

