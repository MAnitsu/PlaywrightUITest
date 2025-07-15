# UI Test Automation with Python & Playwright

This project automates UI tests for [the-internet.herokuapp.com](https://the-internet.herokuapp.com/) using Python, pytest, and Playwright.  

It’s designed as a learning and portfolio project for UI test automation.

---

## 📂 Project Structure

- `venv/` → Environment directory
- `tests/` → Contains all test files
- `conftest.py` → Defines pytest fixtures for browser and page setup
- `requirements.txt` → Python dependencies
- `README.md` → Documentation

---

## ✅ Prerequisites

- Python ≥ 3.9
- Git

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/MAnitsu/PlaywrightUITest.git
cd PlaywrightUITest
```

### 2. Create a Virtual Environment
```bash
# Windows:
python -m venv venv
venv\Scripts\activate # activates environment

# macOS/Linux:
python3 -m venv venv
source venv/bin/activate # activates environment
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers
```bash
playwright install
```
## 🧪 Running Tests
Run all tests:
```bash
pytest
```
Run a specific test file:
```bash
pytest tests/test_login.py
```
Run tests with detailed output:
```bash
pytest -v
```

## 📄 How to Create New Tests

### 1. Create a new file in tests/:
```bash
tests/test_new_feature.py
```
### 2. Import the page fixture:
```python
def test_something(page):
    page.goto("https://the-internet.herokuapp.com/")
    # Your test actions
    assert page.title() == "The Internet"
```

### 3. Use Playwright commands:
- page.goto(url)
- page.fill(selector, text)
- page.click(selector)
- page.locator(selector).is_visible()
- page.locator(selector).inner_text()

## 🔎 Playwright Locator Tips

Examples:
```python
page.locator("#username")
page.locator(".button")
page.locator("button[type='submit']")
```

## 📂 Managing Test Data (will expand on this later with a script that creates test data)
For file upload tests, create a dummy file:
```bash
echo "Hello World" > testfile.txt
```

## 🚀 Ways to Expand This Project
✅ Add tests for more pages on the-internet.herokuapp.com

✅ Implement the Page Object Model (POM)

✅ Use pytest parametrize to test multiple inputs

✅ Generate HTML test reports (e.g. pytest-html)

✅ Integrate with GitHub Actions for Continuous Integration

✅ Run tests in headless mode for speed

✅ Test on multiple browsers (Chromium, Firefox, WebKit)

## 📝 Useful Commands
Run Playwright Codegen (record actions):
```bash
playwright codegen https://the-internet.herokuapp.com/
```
Update requirements.txt:
```bash
pip freeze > requirements.txt
```
Deactivate virtual environment:
```bash
deactivate
```

## 👨‍💻 Author
Manitsu

GitHub Profile: https://github.com/MAnitsu
