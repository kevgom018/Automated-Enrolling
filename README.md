# Automated Enrolling

This project automates the process of enrolling in university courses by remotely logging into the student enrollment system over SSH and navigating the interactive menu system using `pexpect`.

## 🔐 What It Does

- Logs into your university's server using SSH.
- Enters your student credentials (student number, PIN, SSN, and DOB).
- Navigates the terminal-based enrollment menus.
- Automatically selects the semester, courses, and sections based on a configuration file.

---

## 🛠️ Setup

### 1. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
```

### 2. Install dependencies

```bash
pip install pexpect
```

---

## 📁 File Structure

```
Automated Enrolling/
├── main.py                  # Entry point for automation
├── credentials.json         # Sensitive info (never commit this!)
├── schedule.json            # Desired semester, courses, and sections
├── README.md
```

---

## 🔐 Credentials File

Create a file named `credentials.json` (not committed to Git) like this:

```json
{
  "student_number": "12345678",
  "pin": "1234",
  "social_security": "123-45-6789",
  "dob": "MM-DD-YYYY"
}
```

> ⚠️ **Do not commit this file** — add it to your `.gitignore`.

---

## 📅 Schedule File

Use a structured JSON file for clarity and flexibility:

```json
{
  "semester": "2025S1",
  "courses": [
    {
      "code": "CIIC3011",
      "section": "030"
    },
    {
      "code": "MATE3032",
      "section": "020"
    }
  ]
}
```

---

## 🚀 Running the Script

```bash
python main.py
```

Make sure `credentials.json` and `courses.json` are present in the same folder.

---

## 📄 License

MIT License — feel free to modify for personal use.