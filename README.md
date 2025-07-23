# 📘 Leetcode Question Scraper

This repository contains a Python script to **scrape Leetcode questions** and store relevant information such as title, difficulty, and URL into a CSV file.

## 🚀 Features

- Scrapes **all public Leetcode questions**
- Saves data in a structured **CSV file**
- Captures the following fields:
  - Question title
  - Difficulty (Easy / Medium / Hard)
  - Slug (used for URL generation)
  - Link to the question
  - Status (if logged in)

---

## 🛠 Requirements

Make sure you have Python installed (preferably `3.8+`), then install the required packages:

```bash
pip install -r requirements.txt
```

## 📂 File Structure

```
Leetcode-Question-Scrapping/
│
├── script.py       # Main script to fetch Leetcode question data
├── requirements.txt          # Python dependencies
└── README.md                 # Documentation
```

---

## ⚙️ How to Use

### 1. Clone the repository:
```bash
git clone https://github.com/includeNayan/Leetcode-Question-Scrapping.git
cd Leetcode-Question-Scrapping
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run the scraper:
```bash
python leetcode_scraper.py
```
