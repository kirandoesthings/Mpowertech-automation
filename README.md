# MUDU LMS Automation — Playwright + Allure

End-to-end test automation for the MUDU LMS portal.  
Covers: **Student** and **Faculty/HOD** modules.  
Stack: Python · Playwright · pytest · Allure Reports · GitHub Actions

---

## Project Structure

```
Mpowertech-automation/
├── pages/
│   ├── base_page.py          ← shared Playwright actions (all pages inherit this)
│   ├── student/
│   │   ├── login_page.py
│   │   └── dashboard_page.py
│   └── faculty_hod/
│       ├── login_page.py
│       └── dashboard_page.py
├── tests/
│   ├── student/
│   │   ├── test_student_login.py
│   │   └── test_student_dashboard.py
│   └── faculty_hod/
│       ├── test_faculty_login.py
│       └── test_faculty_dashboard.py
├── reports/allure-results/   ← gitignored, generated on run
├── screenshots/              ← gitignored, auto-saved on failure
├── conftest.py
├── pytest.ini
├── requirements.txt
└── .github/workflows/
    ├── admin_tests.yml
    ├── faculty_hod_tests.yml
    └── student_tests.yml
```

---

## Local Setup

### 1. Clone and create virtual environment

```powershell
git clone https://github.com/kirandoesthings/Mpowertech-automation.git
cd Mpowertech-automation
python -m venv venv
venv\Scripts\activate        # Windows PowerShell
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
playwright install chromium
```

### 3. Configure environment

```powershell
copy .env.example .env       # Windows
# Edit .env with real credentials — never commit this file
```

### 4. Run tests

```powershell
# All student tests
pytest tests/student/ -v

# All faculty tests
pytest tests/faculty_hod/ -v

# Specific test file
pytest tests/student/test_student_login.py -v

# With Allure report generation
pytest tests/student/ --alluredir=reports/allure-results
allure serve reports/allure-results
```

---

## CI/CD — GitHub Actions

Each module has its own workflow that triggers **only when its files change**:

| Workflow | Trigger Path |
|---|---|
| `student_tests.yml` | `pages/student/**`, `tests/student/**` |
| `faculty_hod_tests.yml` | `pages/faculty_hod/**`, `tests/faculty_hod/**` |
| `admin_tests.yml` | `pages/admin/**`, `tests/admin/**` |

### Required GitHub Secrets

Go to **Settings → Secrets → Actions** and add:

```
BASE_URL
STUDENT_EMAIL
STUDENT_PASSWORD
FACULTY_EMAIL
FACULTY_PASSWORD
ADMIN_EMAIL
ADMIN_PASSWORD
```

---

## Adding New Tests

1. Add a new page object in `pages/<module>/your_page.py` extending `BasePage`
2. Add a new test file in `tests/<module>/test_your_feature.py`
3. Use `@allure.feature`, `@allure.story`, `@allure.severity` decorators
4. Push — CI triggers automatically

---

## Adding a New Module (e.g., Admin)

```
pages/admin/
    __init__.py
    login_page.py
    dashboard_page.py
    user_management_page.py
    ...
tests/admin/
    __init__.py
    test_admin_login.py
    test_user_management.py
    ...
```
# MUDU LMS Automation — Playwright + Allure

End-to-end test automation for the MUDU LMS portal.  
Covers: **Student** and **Faculty/HOD** modules.  
Stack: Python · Playwright · pytest · Allure Reports · GitHub Actions

---

## Project Structure

```
Mpowertech-automation/
├── pages/
│   ├── base_page.py          ← shared Playwright actions (all pages inherit this)
│   ├── student/
│   │   ├── login_page.py
│   │   └── dashboard_page.py
│   └── faculty_hod/
│       ├── login_page.py
│       └── dashboard_page.py
├── tests/
│   ├── student/
│   │   ├── test_student_login.py
│   │   └── test_student_dashboard.py
│   └── faculty_hod/
│       ├── test_faculty_login.py
│       └── test_faculty_dashboard.py
├── reports/allure-results/   ← gitignored, generated on run
├── screenshots/              ← gitignored, auto-saved on failure
├── conftest.py
├── pytest.ini
├── requirements.txt
└── .github/workflows/
    ├── admin_tests.yml
    ├── faculty_hod_tests.yml
    └── student_tests.yml
```

---

## Local Setup

### 1. Clone and create virtual environment

```powershell
git clone https://github.com/kirandoesthings/Mpowertech-automation.git
cd Mpowertech-automation
python -m venv venv
venv\Scripts\activate        # Windows PowerShell
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
playwright install chromium
```

### 3. Configure environment

```powershell
copy .env.example .env       # Windows
# Edit .env with real credentials — never commit this file
```

### 4. Run tests

```powershell
# All student tests
pytest tests/student/ -v

# All faculty tests
pytest tests/faculty_hod/ -v

# Specific test file
pytest tests/student/test_student_login.py -v

# With Allure report generation
pytest tests/student/ --alluredir=reports/allure-results
allure serve reports/allure-results
```

---

## CI/CD — GitHub Actions

Each module has its own workflow that triggers **only when its files change**:

| Workflow | Trigger Path |
|---|---|
| `student_tests.yml` | `pages/student/**`, `tests/student/**` |
| `faculty_hod_tests.yml` | `pages/faculty_hod/**`, `tests/faculty_hod/**` |
| `admin_tests.yml` | `pages/admin/**`, `tests/admin/**` |

### Required GitHub Secrets

Go to **Settings → Secrets → Actions** and add:

```
BASE_URL
STUDENT_EMAIL
STUDENT_PASSWORD
FACULTY_EMAIL
FACULTY_PASSWORD
ADMIN_EMAIL
ADMIN_PASSWORD
```

---

## Adding New Tests

1. Add a new page object in `pages/<module>/your_page.py` extending `BasePage`
2. Add a new test file in `tests/<module>/test_your_feature.py`
3. Use `@allure.feature`, `@allure.story`, `@allure.severity` decorators
4. Push — CI triggers automatically

---

## Adding a New Module (e.g., Admin)

```
pages/admin/
    __init__.py
    login_page.py
    dashboard_page.py
    user_management_page.py
    ...
tests/admin/
    __init__.py
    test_admin_login.py
    test_user_management.py
    ...
```

Follow the same POM pattern as student/faculty.
